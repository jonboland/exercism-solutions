from collections import defaultdict
from operator import itemgetter


HEADINGS = ("Team".ljust(30), "MP", " W", " D", " L", " P")
SEP = " | "
HEADER_ROW = SEP.join(HEADINGS)


def tally(rows):
    """Tallies the results of a football competition."""
    rows_split = split_rows(rows)
    individual_scores = convert_rows(rows_split)
    grouped_scores = group_scores(individual_scores)
    overall_stats = calculate_stats(grouped_scores)
    overall_stats = order_stats(overall_stats)
    return format_table(overall_stats)


def split_rows(rows):
    for row in rows:
        yield row.split(";")


def convert_rows(rows_split):
    """Converts rows into individual scores for each team."""
    for team_one, team_two, result in rows_split:
        if result == "win":
            yield (team_one, 3)
            yield (team_two, 0)
        elif result == "draw":
            yield (team_one, 1)
            yield (team_two, 1)
        else:
            yield (team_one, 0)
            yield (team_two, 3)


def group_scores(individual_scores):
    """Groups individual scores together by team."""
    grouped_scores = defaultdict(list)

    for team, score in individual_scores:
        grouped_scores[team].append(score)

    for row in grouped_scores.items():
        yield row


def calculate_stats(grouped_scores):
    """Calculates team statistics based on grouped scores."""
    overall_stats = []

    for team, scores in grouped_scores:
        team_stats = [team.ljust(30)]  # Team Name
        team_stats.extend(
            (
                len(scores),  # Matches Played
                scores.count(3),  # Wins
                scores.count(1),  # Draws
                scores.count(0),  # Losses
                sum(scores),  # Points
            )
        )
        overall_stats.append(team_stats)

    return overall_stats


def order_stats(overall_stats):
    """
    Sorts team statistics by points in descending order,
    and alphabetically if points are tied.
    """
    overall_stats.sort()
    overall_stats.sort(key=itemgetter(5), reverse=True)

    for row in overall_stats:
        yield row


def format_table(overall_stats):
    """Formats statistics into table with headings."""
    formatted_table = [HEADER_ROW]

    for row in overall_stats:
        justified_text = (f"{element:2}" for element in row)
        formatted_row = SEP.join(justified_text)
        formatted_table.append(formatted_row)

    return formatted_table
