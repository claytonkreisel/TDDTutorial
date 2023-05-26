class Score:
    score: float
    home: bool

    def __init__(self, score: float, home: bool):
        self.score = score
        self.home = home

    def __eq__(self, other):
        if not isinstance(other, Score):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.score == other.score and self.home == other.home


def get_scores_to_tally(scores: [Score]):
    # Sort provided scores from top score to bottom score
    scores.sort(key=lambda score: score.score, reverse=True)

    # Find next 6 top scores with at least 3 being away meets
    nqs_scores: [Score] = []

    for score in scores:
        if len(nqs_scores) == 6:
            break
        if score.home:
            if len([nqs_score for nqs_score in nqs_scores if nqs_score.home]) <= 3:
                nqs_scores.append(score)
        else:
            nqs_scores.append(score)

    # Remove top ncaa_gymnastics score to bring list to 5 total
    nqs_scores.pop(0)
    return nqs_scores


def factor_nqs(scores: [Score]):
    return sum([score.score for score in scores]) / len(scores)


def get_nqs(scores: [Score]):
    return factor_nqs(get_scores_to_tally(scores))
