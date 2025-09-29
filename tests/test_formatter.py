from prayer_text_reformatter import reformat_prayer_text


def test_reformat_example_text():
    raw = (
        "Nov 16, 2024: Nepal – Caste Discrimination and the Church\n\n"
        "In Nepal, the caste system has long created division, excluding many from opportunities and causing discrimination and injustice. As the church grows, it has the opportunity to be a powerful witness of unity, breaking down caste barriers and showing that in Christ, all are equally valued and loved. Still some who are in Christ have not accepted this revelation of oneness.\n\n"
        "Pray for the church in Nepal to be a place where caste barriers are broken, demonstrating the equal value of all people in Christ.\n\n"
        "Ask for believers to lead by example, promoting love and inclusion in their communities.\n\n"
        "Pray for those who have suffered under caste discrimination to find acceptance, healing, and hope within the body of Christ.\n"
    )

    expected = (
        "*Nov 16, 2024 | Nepal – Caste Discrimination and the Church*\n\n"
        "In Nepal, the caste system has long created division, excluding many from opportunities and causing discrimination and injustice. As the church grows, it has the opportunity to be a powerful witness of unity, breaking down caste barriers and showing that in Christ, all are equally valued and loved. Still some who are in Christ have not accepted this revelation of oneness.\n\n"
        "- Pray for the church in Nepal to be a place where caste barriers are broken, demonstrating the equal value of all people in Christ.\n\n"
        "- Ask for believers to lead by example, promoting love and inclusion in their communities.\n\n"
        "- Pray for those who have suffered under caste discrimination to find acceptance, healing, and hope within the body of Christ."
    )

    assert reformat_prayer_text(raw) == expected


def test_missing_header_raises_value_error():
    raw = "\n\nNo header here."
    try:
        reformat_prayer_text(raw)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError when header is missing")
