from langguesser.guesser import _diff
from langguesser.guesser import _calculate_distance
from langguesser.guesser import _closest_match


def test_diff():
    assert _diff(1.0, 0.2) == 0.8
    assert _diff(0.2, 1.0) == 0.8
    assert _diff(0.0, 0.0) == 0.0
    assert _diff(1.0, 2.0) == 1.0


def test_calculate_distance():
    sig_x = {"char_freq": {"a": 0.2, "b": 0.2, "c": 0.2, "d": 0.2, "e": 0.2,}}
    sig_y = {"char_freq": {"a": 0.1, "b": 0.1, "c": 0.2, "d": 0.3, "e": 0.3,}}
    assert round(_calculate_distance(sig_x, sig_y), 2) == 0.4
    assert round(_calculate_distance(sig_y, sig_x), 2) == 0.4
    assert round(_calculate_distance(sig_y, sig_y), 2) == 0.0
    assert round(_calculate_distance(sig_x, sig_x), 2) == 0.0


def test_closest_match_zh():
    language_signatures = list()
    language_signatures.append(
        {"language": "chinese (traditional)", "char_freq": {"愛": 1.0}}
    )
    language_signatures.append(
        {"language": "chinese (simplified)", "char_freq": {"爱": 1.0}}
    )
    signature = {"char_freq": {"愛": 0.7, "你": 0.2, "我": 0.1}}
    assert _closest_match(signature, language_signatures) == "chinese (traditional)"


def test_closest_match():
    language_signatures = list()
    language_signatures.append(
        {"language": "lang_a", "char_freq": {"a": 0.4, "b": 0.5, "c": 0.1}}
    )
    language_signatures.append(
        {"language": "lang_b", "char_freq": {"a": 0.4, "b": 0.1, "c": 0.5}}
    )
    signature_a = {"char_freq": {"a": 0.5, "b": 0.5,}}
    signature_b = {"char_freq": {"a": 0.5, "b": 0.1, "c": 0.4}}
    assert _closest_match(signature_a, language_signatures) == "lang_a"
    assert _closest_match(signature_b, language_signatures) == "lang_b"
