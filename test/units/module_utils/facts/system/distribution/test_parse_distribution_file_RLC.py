# Copyright: Contributors to the Ansible project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

import pytest

from ansible.module_utils.facts.system.distribution import DistributionFiles


OS_RELEASE_RLC_PRO = """NAME="Rocky Linux from CIQ"
VERSION="9.7 (Blue Onyx)"
ID="rocky"
VERSION_ID="9.7"
VARIANT="Pro"
VARIANT_ID="pro"
CPE_NAME="cpe:2.3:o:ciq:rocky_linux_from_ciq_pro:9.7"
"""

OS_RELEASE_RLC_PRO_AI = """NAME="Rocky Linux from CIQ"
VERSION="9.7 (Blue Onyx)"
ID="rocky"
VERSION_ID="9.7"
VARIANT="Pro AI"
VARIANT_ID="pro_ai"
CPE_NAME="cpe:2.3:o:ciq:rocky_linux_from_ciq_pro_ai:9.7"
"""

OS_RELEASE_RLC_PRO_HARDENED = """NAME="Rocky Linux from CIQ"
VERSION="9.7 (Blue Onyx)"
ID="rocky"
VERSION_ID="9.7"
VARIANT="Pro Hardened"
VARIANT_ID="pro-hardened"
CPE_NAME="cpe:2.3:o:ciq:rocky_linux_from_ciq_pro_hardened:9.7"
"""

OS_RELEASE_RLC_PRO_HARDENED_LTS = """NAME="Rocky Linux from CIQ"
VERSION="9.6 (Blue Onyx)"
ID="rocky"
VERSION_ID="9.6"
VARIANT="Pro Hardened LTS"
VARIANT_ID="pro-hardened-lts"
CPE_NAME="cpe:2.3:o:ciq:rocky_linux_from_ciq_pro_hardened_lts:9.6"
"""

OS_RELEASE_RLC_PLUS = """NAME="Rocky Linux from CIQ"
VERSION="9.7 (Blue Onyx)"
ID="rocky"
VERSION_ID="9.7"
CPE_NAME="cpe:2.3:o:ciq:rocky_linux_from_ciq:9.7"
"""

OS_RELEASE_RLC_LTS = """NAME="Rocky Linux from CIQ - LTS"
VERSION="9.6 (Blue Onyx)"
ID="rocky"
VERSION_ID="9.6"
CPE_NAME="cpe:2.3:o:ciq:rocky_linux_from_ciq_lts:9.6"
"""

OS_RELEASE_ROCKY_STOCK = """NAME="Rocky Linux"
VERSION="9.2 (Blue Onyx)"
ID="rocky"
VERSION_ID="9.2"
CPE_NAME="cpe:/o:rocky:rocky:9::baseos"
"""

OS_RELEASE_FEDORA = """NAME="Fedora Linux"
VERSION="41 (Workstation Edition)"
ID=fedora
VERSION_ID=41
CPE_NAME="cpe:/o:fedoraproject:fedora:41"
"""


@pytest.mark.parametrize(
    'data, expected_parsed, expected_facts',
    [
        pytest.param(
            OS_RELEASE_RLC_PRO,
            True,
            {
                'distribution': 'Rocky Linux from CIQ',
                'distribution_version': '9.7',
                'distribution_major_version': '9',
                'distribution_minor_version': '7',
                'distribution_variant': 'pro',
                'distribution_release': 'Blue Onyx',
            },
            id='rlc-pro-9',
        ),
        pytest.param(
            OS_RELEASE_RLC_PRO_AI,
            True,
            {
                'distribution': 'Rocky Linux from CIQ',
                'distribution_version': '9.7',
                'distribution_major_version': '9',
                'distribution_minor_version': '7',
                'distribution_variant': 'pro_ai',
                'distribution_release': 'Blue Onyx',
            },
            id='rlc-ai-9',
        ),
        pytest.param(
            OS_RELEASE_RLC_PRO_HARDENED,
            True,
            {
                'distribution': 'Rocky Linux from CIQ',
                'distribution_version': '9.7',
                'distribution_major_version': '9',
                'distribution_minor_version': '7',
                'distribution_variant': 'pro-hardened',
                'distribution_release': 'Blue Onyx',
            },
            id='rlc-h-9',
        ),
        pytest.param(
            OS_RELEASE_RLC_PRO_HARDENED_LTS,
            True,
            {
                'distribution': 'Rocky Linux from CIQ',
                'distribution_version': '9.6',
                'distribution_major_version': '9',
                'distribution_minor_version': '6',
                'distribution_variant': 'pro-hardened-lts',
                'distribution_release': 'Blue Onyx',
            },
            id='rlc-pro-h-9.6-lts',
        ),
        pytest.param(
            OS_RELEASE_RLC_PLUS,
            True,
            {
                'distribution': 'Rocky Linux from CIQ',
                'distribution_version': '9.7',
                'distribution_major_version': '9',
                'distribution_minor_version': '7',
                'distribution_release': 'Blue Onyx',
            },
            id='rlc-plus-9-no-variant',
        ),
        pytest.param(
            OS_RELEASE_RLC_LTS,
            True,
            {
                'distribution': 'Rocky Linux from CIQ',
                'distribution_version': '9.6',
                'distribution_major_version': '9',
                'distribution_minor_version': '6',
                'distribution_variant': 'lts',
                'distribution_release': 'Blue Onyx',
            },
            id='rlc-lts-9.6-variant-from-cpe',
        ),
        pytest.param(
            OS_RELEASE_ROCKY_STOCK,
            False,
            {},
            id='stock-rocky-no-match',
        ),
        pytest.param(
            OS_RELEASE_FEDORA,
            False,
            {},
            id='fedora-no-match',
        ),
    ],
)
def test_parse_distribution_file_RLC(mock_module, data, expected_parsed, expected_facts):
    distribution = DistributionFiles(module=mock_module)
    parsed, facts = distribution.parse_distribution_file_RLC(
        name='RLC',
        data=data,
        path='/etc/os-release',
        collected_facts=None,
    )
    assert parsed == expected_parsed
    assert facts == expected_facts
