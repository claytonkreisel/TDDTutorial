from ncaa_gymnastics.app.nqs import Score, get_scores_to_tally, factor_nqs, get_nqs

team1 = [
    Score(score=197.125, home=False),
    Score(score=196.875, home=False),
    Score(score=197.225, home=True),
    Score(score=197.725, home=False),
    Score(score=196.550, home=True),
    Score(score=198.025, home=False),
    Score(score=197.775, home=True),
    Score(score=197.675, home=False),
    Score(score=196.625, home=False),
    Score(score=197.025, home=True),
]


def test_team1_get_scores_to_tally():
    team1_scores = get_scores_to_tally(team1)
    assert len(team1_scores) == 5
    assert len([score for score in team1_scores if not score.home]) == 3
    assert len([score for score in team1_scores if score.home]) == 2
    assert Score(score=197.775, home=True) in team1_scores
    assert Score(score=197.675, home=False) in team1_scores
    assert Score(score=197.125, home=False) in team1_scores
    assert Score(score=197.225, home=True) in team1_scores
    assert Score(score=197.725, home=False) in team1_scores


def test_factor_nqs():
    assert factor_nqs(get_scores_to_tally(team1)) == 197.505


def test_get_nqs():
    assert get_nqs(team1) == 197.505


def test_main():
    pass
