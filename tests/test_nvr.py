from __future__ import annotations

import pytest

from pkgps import NEVR, NEVRA, NVR, NVRA, MalformedCoordinates


@pytest.mark.parametrize(
    "nvr,expected",
    [
        (
            "kernel-6.8.5-301.fc40",
            NVR(name="kernel", version="6.8.5", release="301.fc40"),
        ),
        (
            "libstdc++-14.0.1-0.15.fc40",
            NVR(name="libstdc++", version="14.0.1", release="0.15.fc40"),
        ),
        (
            "gcc-c++-14.0.1-0.15.fc40",
            NVR(
                name="gcc-c++",
                version="14.0.1",
                release="0.15.fc40",
            ),
        ),
        (
            "perl-Text-Tabs+Wrap-2024.001-1.fc40",
            NVR(
                name="perl-Text-Tabs+Wrap",
                version="2024.001",
                release="1.fc40",
            ),
        ),
        (
            "containers-common-0.58.0-2.fc40",
            NVR(
                name="containers-common",
                version="0.58.0",
                release="2.fc40",
            ),
        ),
    ],
)
def test_nvr_successful_parse(nvr: str, expected: NVR):
    actual = NVR.from_string(nvr)
    assert actual == expected


def test_nvr_unpacking_behavior():
    n, v, r = NVR.from_string("curl-8.6.0-7.fc40")
    assert n == "curl"
    assert v == "8.6.0"
    assert r == "7.fc40"


def test_nvr_to_dict():
    nvr = NVR.from_string("curl-8.6.0-7.fc40")
    assert nvr.to_dict() == {
        "name": "curl",
        "version": "8.6.0",
        "release": "7.fc40",
    }


@pytest.mark.parametrize(
    "nvr,type_",
    [
        ("11.0.0-1.fc40", NVR),
        ("test-1.fc40", NEVR),
        ("kernel", NVRA),
        ("kernel.1.1.1.1.fc40", NEVRA),
    ],
)
def test_unsuccessful_parse(nvr: str, type_: type[NVR]):
    with pytest.raises(MalformedCoordinates):
        type_.from_string(nvr)


@pytest.mark.parametrize(
    "nevr,expected",
    [
        (
            "dbus-1:1.14.10-3.fc40",
            NEVR(name="dbus", epoch=1, version="1.14.10", release="3.fc40"),
        ),
        (
            "NetworkManager-1:1.46.0-2.fc40",
            NEVR(
                name="NetworkManager",
                epoch=1,
                version="1.46.0",
                release="2.fc40",
            ),
        ),
        (
            "emacs-1:29.2-3.fc40",
            NEVR(
                name="emacs",
                epoch=1,
                version="29.2",
                release="3.fc40",
            ),
        ),
    ],
)
def test_nevr_successful_parse(nevr: str, expected: NEVR):
    actual = NEVR.from_string(nevr)
    assert actual == expected


@pytest.mark.parametrize(
    "nevr,expected",
    [
        (
            NEVR(name="dbus", version="1.14.10", release="3.fc40", epoch=1),
            "dbus-1:1.14.10-3.fc40",
        ),
        (
            NEVR(name="NetworkManager", version="1.46.0", release="2.fc40", epoch=1),
            "NetworkManager-1:1.46.0-2.fc40",
        ),
        (
            NEVR(name="emacs", version="29.2", release="3.fc40", epoch=1),
            "emacs-1:29.2-3.fc40",
        ),
    ],
)
def test_nevr_to_string(nevr: NEVR, expected: str):
    assert str(nevr) == expected


def test_nevr_unpacking_behavior():
    n, e, v, r = NEVR.from_string("curl-1:8.6.0-7.fc40")
    assert n == "curl"
    assert e == 1
    assert v == "8.6.0"
    assert r == "7.fc40"


def test_nevr_to_dict():
    nevr = NEVR.from_string("curl-1:8.6.0-7.fc40")
    assert nevr.to_dict() == {
        "name": "curl",
        "epoch": 1,
        "version": "8.6.0",
        "release": "7.fc40",
    }


@pytest.mark.parametrize(
    "nvra,expected",
    [
        (
            "kernel-6.8.5-301.fc40.ppc64le",
            NVRA(name="kernel", version="6.8.5", release="301.fc40", arch="ppc64le"),
        ),
        (
            "libstdc++-14.0.1-0.15.fc40.ppc64le",
            NVRA(
                name="libstdc++", version="14.0.1", release="0.15.fc40", arch="ppc64le"
            ),
        ),
        (
            "gcc-c++-14.0.1-0.15.fc40.ppc64le",
            NVRA(name="gcc-c++", version="14.0.1", release="0.15.fc40", arch="ppc64le"),
        ),
        (
            "perl-Text-Tabs+Wrap-2024.001-1.fc40.ppc64le",
            NVRA(
                name="perl-Text-Tabs+Wrap",
                version="2024.001",
                release="1.fc40",
                arch="ppc64le",
            ),
        ),
        (
            "containers-common-0.58.0-2.fc40.aarch64",
            NVRA(
                name="containers-common",
                version="0.58.0",
                release="2.fc40",
                arch="aarch64",
            ),
        ),
    ],
)
def test_nvra_successful_parse(nvra: str, expected: NVRA):
    actual = NVRA.from_string(nvra)
    assert actual == expected


@pytest.mark.parametrize(
    "nvra,expected",
    [
        (
            NVRA(name="kernel", version="6.8.5", release="301.fc40", arch="ppc64le"),
            "kernel-6.8.5-301.fc40.ppc64le",
        ),
        (
            NVRA(
                name="libstdc++", version="14.0.1", release="0.15.fc40", arch="ppc64le"
            ),
            "libstdc++-14.0.1-0.15.fc40.ppc64le",
        ),
        (
            NVRA(name="gcc-c++", version="14.0.1", release="0.15.fc40", arch="ppc64le"),
            "gcc-c++-14.0.1-0.15.fc40.ppc64le",
        ),
        (
            NVRA(
                name="perl-Text-Tabs+Wrap",
                version="2024.001",
                release="1.fc40",
                arch="ppc64le",
            ),
            "perl-Text-Tabs+Wrap-2024.001-1.fc40.ppc64le",
        ),
        (
            NVRA(
                name="containers-common",
                version="0.58.0",
                release="2.fc40",
                arch="aarch64",
            ),
            "containers-common-0.58.0-2.fc40.aarch64",
        ),
    ],
)
def test_nvra_to_string(nvra: NVRA, expected: str):
    assert str(nvra) == expected


def test_nvra_unpacking_behavior():
    n, v, r, a = NVRA.from_string("curl-8.6.0-7.fc40.aarch64")
    assert n == "curl"
    assert v == "8.6.0"
    assert r == "7.fc40"
    assert a == "aarch64"


def test_nvra_to_dict():
    nvra = NVRA.from_string("curl-8.6.0-7.fc40.aarch64")
    assert nvra.to_dict() == {
        "name": "curl",
        "version": "8.6.0",
        "release": "7.fc40",
        "arch": "aarch64",
    }


@pytest.mark.parametrize(
    "nevra,expected",
    [
        (
            "dbus-1:1.14.10-3.fc40.aarch64",
            NEVRA(
                name="dbus",
                version="1.14.10",
                release="3.fc40",
                arch="aarch64",
                epoch=1,
            ),
        ),
        (
            "NetworkManager-1:1.46.0-2.fc40.x86_64",
            NEVRA(
                name="NetworkManager",
                version="1.46.0",
                release="2.fc40",
                arch="x86_64",
                epoch=1,
            ),
        ),
        (
            "emacs-1:29.2-3.fc40.ppc64le",
            NEVRA(
                name="emacs", version="29.2", release="3.fc40", arch="ppc64le", epoch=1
            ),
        ),
    ],
)
def test_nevra_successful_parse(nevra: str, expected: NEVRA):
    actual = NEVRA.from_string(nevra)
    assert actual == expected


@pytest.mark.parametrize(
    "nevra,expected",
    [
        (
            NEVRA(
                name="dbus",
                version="1.14.10",
                release="3.fc40",
                arch="aarch64",
                epoch=1,
            ),
            "dbus-1:1.14.10-3.fc40.aarch64",
        ),
        (
            NEVRA(
                name="NetworkManager",
                version="1.46.0",
                release="2.fc40",
                arch="x86_64",
                epoch=1,
            ),
            "NetworkManager-1:1.46.0-2.fc40.x86_64",
        ),
        (
            NEVRA(
                name="emacs", version="29.2", release="3.fc40", arch="ppc64le", epoch=1
            ),
            "emacs-1:29.2-3.fc40.ppc64le",
        ),
    ],
)
def test_nevra_to_string(nevra: NEVRA, expected: str):
    assert str(nevra) == expected


def test_nevra_unpacking_behavior():
    n, e, v, r, a = NEVRA.from_string("curl-1:8.6.0-7.fc40.aarch64")
    assert n == "curl"
    assert e == 1
    assert v == "8.6.0"
    assert r == "7.fc40"
    assert a == "aarch64"


def test_nevra_to_dict():
    nevra = NEVRA.from_string("curl-1:8.6.0-7.fc40.aarch64")
    assert nevra.to_dict() == {
        "name": "curl",
        "epoch": 1,
        "version": "8.6.0",
        "release": "7.fc40",
        "arch": "aarch64",
    }


@pytest.mark.parametrize(
    "coordinate,receiver,expected",
    [
        (
            "dbus-1.14.10-3.fc40",
            NVR,
            NVR(name="dbus", version="1.14.10", release="3.fc40"),
        ),
        (None, NVR, None),
        (
            "dbus-1.14.10-3.fc40.aarch64",
            NVRA,
            NVRA(name="dbus", version="1.14.10", release="3.fc40", arch="aarch64"),
        ),
        (None, NVRA, None),
        (
            "dbus-1:1.14.10-3.fc40",
            NEVR,
            NEVR(name="dbus", epoch=1, version="1.14.10", release="3.fc40"),
        ),
        (None, NEVR, None),
        (
            "dbus-1:1.14.10-3.fc40.aarch64",
            NEVRA,
            NEVRA(
                name="dbus",
                epoch=1,
                version="1.14.10",
                release="3.fc40",
                arch="aarch64",
            ),
        ),
        (None, NEVRA, None),
    ],
)
def test_from_string_or_none(
    coordinate: str, receiver: type[NVR], expected: NVR | None
):
    actual = receiver.from_string_or_none(coordinate)
    assert actual == expected
    if expected is not None:
        assert isinstance(actual, receiver)


# The following code was generated by Claude 4.5 Sonnet
####################################### Begin: AI Generated Code ###################################


def test_nevr_to_nvr():
    """Test NEVR.to_nvr() discards epoch information."""
    nevr = NEVR.from_string("curl-1:8.6.0-7.fc40")
    nvr = nevr.to_nvr()

    assert isinstance(nvr, NVR)
    assert nvr.name == "curl"
    assert nvr.version == "8.6.0"
    assert nvr.release == "7.fc40"
    assert str(nvr) == "curl-8.6.0-7.fc40"


def test_nevr_to_nvr_epoch_zero():
    """Test NEVR.to_nvr() works when epoch is 0 (default)."""
    nevr = NEVR(name="test", epoch=0, version="1.0", release="1.fc40")
    nvr = nevr.to_nvr()

    assert isinstance(nvr, NVR)
    assert nvr.name == "test"
    assert nvr.version == "1.0"
    assert nvr.release == "1.fc40"


def test_nvra_to_nvr():
    """Test NVRA.to_nvr() discards architecture information."""
    nvra = NVRA.from_string("curl-8.6.0-7.fc40.aarch64")
    nvr = nvra.to_nvr()

    assert isinstance(nvr, NVR)
    assert nvr.name == "curl"
    assert nvr.version == "8.6.0"
    assert nvr.release == "7.fc40"
    assert str(nvr) == "curl-8.6.0-7.fc40"


def test_nevra_to_nvr():
    """Test NEVRA.to_nvr() discards both epoch and architecture information."""
    nevra = NEVRA.from_string("curl-1:8.6.0-7.fc40.aarch64")
    nvr = nevra.to_nvr()

    assert isinstance(nvr, NVR)
    assert nvr.name == "curl"
    assert nvr.version == "8.6.0"
    assert nvr.release == "7.fc40"
    assert str(nvr) == "curl-8.6.0-7.fc40"


def test_nevra_to_nevr():
    """Test NEVRA.to_nevr() discards architecture information."""
    nevra = NEVRA.from_string("curl-1:8.6.0-7.fc40.aarch64")
    nevr = nevra.to_nevr()

    assert isinstance(nevr, NEVR)
    assert nevr.name == "curl"
    assert nevr.epoch == 1
    assert nevr.version == "8.6.0"
    assert nevr.release == "7.fc40"
    assert str(nevr) == "curl-1:8.6.0-7.fc40"


def test_nevra_to_nvra():
    """Test NEVRA.to_nvra() discards epoch information."""
    nevra = NEVRA.from_string("curl-1:8.6.0-7.fc40.aarch64")
    nvra = nevra.to_nvra()

    assert isinstance(nvra, NVRA)
    assert nvra.name == "curl"
    assert nvra.version == "8.6.0"
    assert nvra.release == "7.fc40"
    assert nvra.arch == "aarch64"
    assert str(nvra) == "curl-8.6.0-7.fc40.aarch64"


@pytest.mark.parametrize(
    "nevra_str,expected_nvr,expected_nevr,expected_nvra",
    [
        (
            "dbus-1:1.14.10-3.fc40.aarch64",
            NVR(name="dbus", version="1.14.10", release="3.fc40"),
            NEVR(name="dbus", epoch=1, version="1.14.10", release="3.fc40"),
            NVRA(name="dbus", version="1.14.10", release="3.fc40", arch="aarch64"),
        ),
        (
            "NetworkManager-1:1.46.0-2.fc40.x86_64",
            NVR(name="NetworkManager", version="1.46.0", release="2.fc40"),
            NEVR(name="NetworkManager", epoch=1, version="1.46.0", release="2.fc40"),
            NVRA(
                name="NetworkManager",
                version="1.46.0",
                release="2.fc40",
                arch="x86_64",
            ),
        ),
        (
            "emacs-1:29.2-3.fc40.ppc64le",
            NVR(name="emacs", version="29.2", release="3.fc40"),
            NEVR(name="emacs", epoch=1, version="29.2", release="3.fc40"),
            NVRA(name="emacs", version="29.2", release="3.fc40", arch="ppc64le"),
        ),
    ],
)
def test_nevra_conversion_methods(
    nevra_str: str, expected_nvr: NVR, expected_nevr: NEVR, expected_nvra: NVRA
):
    """Test all NEVRA conversion methods with various real-world packages."""
    nevra = NEVRA.from_string(nevra_str)

    # Test to_nvr()
    nvr = nevra.to_nvr()
    assert nvr == expected_nvr
    assert isinstance(nvr, NVR)

    # Test to_nevr()
    nevr = nevra.to_nevr()
    assert nevr == expected_nevr
    assert isinstance(nevr, NEVR)

    # Test to_nvra()
    nvra = nevra.to_nvra()
    assert nvra == expected_nvra
    assert isinstance(nvra, NVRA)


####################################### End: AI Generated Code #####################################
