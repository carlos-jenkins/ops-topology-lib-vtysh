# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
VTYSH specification definition and generation module.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

import logging
from os.path import abspath, normpath, dirname, join

from inflection import parameterize, underscore, camelize
from jinja2 import FunctionLoader, Environment, StrictUndefined


log = logging.getLogger(__name__)


VTYSH_SPEC = {
    'config_interface': {
        'doc': 'This is the documentation for this context.',
        'arguments': [
            {
                'name': 'interface',
                'doc': 'blabla'
            },
            {
                'name': 'a',
                'doc': 'babab'
            }
        ],
        'pre_commands': ['config terminal', 'interface {interface}'],
        'post_commands': ['end'],
        'commands': {
            'ip_address': {
                'doc': 'This is the documentation for this command',
                'arguments': [
                    {
                        'name': 'ipv4',
                        'doc': 'blabla'
                    },
                ],
                'command': 'ip address {ipv4}',
                'return': None
            },
            'foo': {
                'doc': 'This is the documentation for this command',
                'arguments': [
                    {
                        'name': 'aa',
                        'doc': 'blabla'
                    },
                ],
                'command': 'echo {aa}',
                'return': 'parse_echo'
            }
        }
    },
    'bar': {
        'doc': 'This is the documentation for this context.',
        'arguments': [
            {
                'name': 'interface',
                'doc': 'blabla'
            },
            {
                'name': 'a',
                'doc': 'babab'
            }
        ],
        'pre_commands': ['config terminal', 'interface {interface}'],
        'post_commands': ['end'],
        'commands': {
            'ip_address': {
                'doc': 'This is the documentation for this command',
                'arguments': [
                    {
                        'name': 'ipv4',
                        'doc': 'blabla'
                    },
                ],
                'command': 'ip address {ipv4}',
                'return': None
            },
            'foo': {
                'doc': 'This is the documentation for this command',
                'arguments': [
                    {
                        'name': 'aa',
                        'doc': 'blabla'
                    },
                ],
                'command': 'echo {aa}',
                'return': 'parse_echo'
            }
        }
    }
}
"""VTYSH Specification as a Python dictionary"""


VTYSH_TEMPLATE = """\
{%- macro param_attrs(attrs) -%}
{% if attrs -%}
, {% for attr in attrs -%}
{{ attr.name|variablize }}
{%- if not loop.last %}, {% endif -%}
{%- endfor %}
{%- endif %}
{%- endmacro -%}
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# WARNING: This is auto-generated, do not manually modify

\"""
vtysh library.
\"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

from .parser import *  # noqa

{% for context_name, context in spec.items() %}
class {{ context_name|objectize }}(object):
    \"""
    {{ context.doc|wordwrap(75)|indent(4) }}
    \"""
    def __init__({{ 'self, enode%s):'|format(param_attrs(context.arguments))|wordwrap(67)|indent(12) }}
        self.enode = enode
        {%- for arg in context.arguments %}
        self.{{ arg.name }} = {{ arg.name }}
        {%- endfor %}

    def __enter__(self):
        commands = \"""\\
        {%- for pre_command in context.pre_commands %}
            {{ pre_command }}
        {%- endfor %}
        \"""

        self.enode.libs.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def __exit__(self):
        commands = \"""\\
        {%- for post_command in context.post_commands %}
            {{ post_command }}
        {%- endfor %}
        \"""

        self.enode.libs.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )
{% for command_name, command in context.commands.items() %}
    def {{ command_name|methodize }}({{ 'self%s):'|format(param_attrs(command.arguments))|wordwrap(67)|indent(12) }}
        \"""
        {{ command.doc|wordwrap(71)|indent(8) }}

        {% for attr in command.arguments -%}
        {{ ':param %s: %s.'|format(attr.name, attr.doc)|wordwrap(75)|indent(5) }}
        {% endfor -%}
        \"""

        {{ "self.enode(
            '%s'.format(**locals()),
            shell='vtysh'
        )"|format(command.command)|assertize(command.return|methodize) }}
{% endfor %}
{%- endfor %}

__all__ = [
{%- for context_name in spec.keys() %}
    '{{ context_name|objectize }}'{% if not loop.last %},{% endif %}
{%- endfor %}
]

"""  # noqa


def filter_objectize(token):
    if token is None:
        return None
    return camelize(underscore(parameterize(underscore(token))))


def filter_methodize(token):
    if token is None:
        return None
    return underscore(parameterize(underscore(token)))


def filter_variablize(token):
    if token is None:
        return None
    return underscore(parameterize(underscore(token)))


def filter_assertize(token, return_function):
    if token is None:
        return None
    if return_function:
        return "return {return_function}({token})".format(**locals())
    return "assert not {}".format(token)


def build():
    """
    Build VTYSH Python module from specification.
    """

    # Build template environment
    def load_template(name):
        templates = {
            'vtysh': VTYSH_TEMPLATE
        }
        return templates[name]

    env = Environment(
        loader=FunctionLoader(load_template),
        undefined=StrictUndefined
    )
    for ftr in ['objectize', 'methodize', 'variablize', 'assertize']:
        env.filters[ftr] = globals()['filter_' + ftr]

    # Render template
    template = env.get_template('vtysh')
    rendered = template.render(
        spec=VTYSH_SPEC
    )

    # Write output
    root = dirname(normpath(abspath(__file__)))

    with open(join(
            root,
            '{}.py'.format('../lib/topology_lib_vtysh/autolib')),
            'w') as module:
        module.write(rendered)


__all__ = ['VTYSH_SPEC']


if __name__ == '__main__':
    build()
