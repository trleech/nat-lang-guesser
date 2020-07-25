def guess_natural_lang(text: str) -> str:
    """
    """
    text_signature = _build_signature(text)
    return _closest_match(text_signature)


def _closest_match(signature: dict, language_signatures: list) -> str:
    """
    Finds a signature with the closest match.
    
    Arguments:
    * signature: dict
    * language_signatures: list of signatures
    """
    current_match_score = 99
    current_match_code = "unknown"
    for known_sig in language_signatures:
        distance = _calculate_distance(signature, known_sig)
        if distance < current_match_score:
            current_match_score = distance
            current_match_code = known_sig["language"]
    return current_match_code


def _calculate_distance(sig_x: dict, sig_y: dict) -> float:
    """
    Calculates the distance between two given signatures.
    
    Arguments:
    * sig_x: dict
    * sig_y: dict
    """
    sum = 0
    for k, v in sig_x["char_freq"].items():
        if k in sig_y["char_freq"]:
            sum += _diff(sig_y["char_freq"][k], v)
        else:
            sum += v

    return sum


def _diff(num_x: float, num_y: float) -> float:
    """
    Returns the absolute difference between two values.
    
    Arguments:
    num_x: float
    num_y: float
    """
    return abs(num_x - num_y)
