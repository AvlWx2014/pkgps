import pytest

from pkgps import NEVR, NEVRA, NVR, NVRA, attrs, pydantic


@pytest.mark.parametrize(
    "receiver",
    [
        NVR,
        attrs.NVR,
        pydantic.NVR,
    ],
)
def test_nvr(receiver):
    actual = receiver(name="curl", version="8.6.0", release="7.fc40")
    assert type(actual) is receiver

    # test from_string
    actual = receiver.from_string("curl-8.6.0-7.fc40")
    assert actual.name == "curl"
    assert actual.version == "8.6.0"
    assert actual.release == "7.fc40"

    # test str
    assert str(actual) == "curl-8.6.0-7.fc40"

    # test iter
    n, v, r = actual
    assert n == "curl"
    assert v == "8.6.0"
    assert r == "7.fc40"

    # test copy constructor
    copy = actual.copy(name="lruc")
    assert copy.name == "lruc"
    assert copy.version == "8.6.0"
    assert copy.release == "7.fc40"
    assert str(copy) == "lruc-8.6.0-7.fc40"

    # test to_dict
    expected = {
        "name": "curl",
        "version": "8.6.0",
        "release": "7.fc40",
    }
    assert actual.to_dict() == expected

    # test from_string_or_none
    actual = receiver.from_string_or_none(None)
    assert actual is None


@pytest.mark.parametrize(
    "receiver",
    [
        NEVR,
        attrs.NEVR,
        pydantic.NEVR,
    ],
)
def test_nevr(receiver):
    actual = receiver(name="curl", epoch=1, version="8.6.0", release="7.fc40")
    assert type(actual) is receiver

    # test from_string
    actual = receiver.from_string("curl-1:8.6.0-7.fc40")
    assert actual.name == "curl"
    assert actual.epoch == 1
    assert actual.version == "8.6.0"
    assert actual.release == "7.fc40"

    # test str
    assert str(actual) == "curl-1:8.6.0-7.fc40"
    copy = actual.copy(epoch=0)
    assert str(copy) == "curl-8.6.0-7.fc40"

    # test iter
    n, e, v, r = actual
    assert n == "curl"
    assert e == 1
    assert v == "8.6.0"
    assert r == "7.fc40"

    # test copy constructor
    copy = actual.copy(name="lruc")
    assert copy.name == "lruc"
    assert copy.epoch == 1
    assert copy.version == "8.6.0"
    assert copy.release == "7.fc40"
    assert str(copy) == "lruc-1:8.6.0-7.fc40"

    # test to_dict
    expected = {
        "name": "curl",
        "epoch": 1,
        "version": "8.6.0",
        "release": "7.fc40",
    }
    assert actual.to_dict() == expected

    # test to_nvr
    expected = NVR(name="curl", version="8.6.0", release="7.fc40")
    assert str(actual.to_nvr()) == str(expected)

    # test from_string_or_none
    actual = receiver.from_string_or_none(None)
    assert actual is None


@pytest.mark.parametrize(
    "receiver",
    [
        NVRA,
        attrs.NVRA,
        pydantic.NVRA,
    ],
)
def test_nvra(receiver):
    actual = receiver(name="curl", version="8.6.0", release="7.fc40", arch="x86_64")
    assert type(actual) is receiver

    # test from_string
    actual = receiver.from_string("curl-8.6.0-7.fc40.x86_64")
    assert actual.name == "curl"
    assert actual.version == "8.6.0"
    assert actual.release == "7.fc40"
    assert actual.arch == "x86_64"

    # test str
    assert str(actual) == "curl-8.6.0-7.fc40.x86_64"

    # test iter
    n, v, r, a = actual
    assert n == "curl"
    assert v == "8.6.0"
    assert r == "7.fc40"
    assert a == "x86_64"

    # test copy constructor
    copy = actual.copy(name="lruc")
    assert copy.name == "lruc"
    assert copy.version == "8.6.0"
    assert copy.release == "7.fc40"
    assert copy.arch == "x86_64"
    assert str(copy) == "lruc-8.6.0-7.fc40.x86_64"

    # test to_dict
    expected = {
        "name": "curl",
        "version": "8.6.0",
        "release": "7.fc40",
        "arch": "x86_64",
    }
    assert actual.to_dict() == expected

    # test to_nvr
    expected = NVR(name="curl", version="8.6.0", release="7.fc40")
    assert str(actual.to_nvr()) == str(expected)

    # test from_string_or_none
    actual = receiver.from_string_or_none(None)
    assert actual is None


@pytest.mark.parametrize(
    "receiver",
    [
        NEVRA,
        attrs.NEVRA,
        pydantic.NEVRA,
    ],
)
def test_nevra(receiver):
    actual = receiver(
        name="curl", epoch=1, version="8.6.0", release="7.fc40", arch="aarch64"
    )
    assert type(actual) is receiver

    # test from_string
    actual = receiver.from_string("curl-1:8.6.0-7.fc40.aarch64")
    assert actual.name == "curl"
    assert actual.epoch == 1
    assert actual.version == "8.6.0"
    assert actual.release == "7.fc40"
    assert actual.arch == "aarch64"

    # test str
    assert str(actual) == "curl-1:8.6.0-7.fc40.aarch64"

    # test iter
    n, e, v, r, a = actual
    assert n == "curl"
    assert e == 1
    assert v == "8.6.0"
    assert r == "7.fc40"
    assert a == "aarch64"

    # test copy constructor
    copy = actual.copy(name="lruc")
    assert copy.name == "lruc"
    assert copy.epoch == 1
    assert copy.version == "8.6.0"
    assert copy.release == "7.fc40"
    assert copy.arch == "aarch64"
    assert str(copy) == "lruc-1:8.6.0-7.fc40.aarch64"

    # test to_dict
    expected = {
        "name": "curl",
        "epoch": 1,
        "version": "8.6.0",
        "release": "7.fc40",
        "arch": "aarch64",
    }
    assert actual.to_dict() == expected

    # test to_nvr
    expected = NVR(name="curl", version="8.6.0", release="7.fc40")
    assert str(actual.to_nvr()) == str(expected)

    # test to_nevr
    expected = NEVR(name="curl", epoch=1, version="8.6.0", release="7.fc40")
    assert str(actual.to_nevr()) == str(expected)

    # test to_nvra
    expected = NVRA(name="curl", version="8.6.0", release="7.fc40", arch="aarch64")
    assert str(actual.to_nvra()) == str(expected)

    # test from_string_or_none
    actual = receiver.from_string_or_none(None)
    assert actual is None
