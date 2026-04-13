"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from typing import Dict

from src.recommender import load_songs, recommend_songs


SAMPLE_USER_PROFILE: Dict = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.82,
}

IMPROVED_USER_PROFILE: Dict = {
    "genres": ["pop", "indie pop", "synthwave"],
    "moods": ["happy", "excited", "moody"],
    "energy": 0.78,
    "tempo_bpm": 118,
    "acousticness": 0.22,
    "valence": 0.74,
    "genre_weight": 2.0,
    "mood_weight": 1.25,
    "tempo_weight": 0.9,
    "acousticness_weight": 0.8,
    "valence_weight": 0.7,
}


def print_profile_review() -> None:
    intense_rock = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.91,
        "tempo_bpm": 152,
        "acousticness": 0.10,
    }
    chill_lofi = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "tempo_bpm": 72,
        "acousticness": 0.86,
    }

    print("Sample user profile:")
    print(SAMPLE_USER_PROFILE)
    print()
    print("Evaluation:")
    print(
        "This profile clearly leans toward upbeat pop because it asks for pop, happy mood, "
        "and high energy."
    )
    print(
        "It can separate intense rock from chill lofi mainly through energy: intense rock is "
        "closer on energy, while chill lofi is far away on both mood and energy."
    )
    print(
        "But it is still too narrow because it ignores tempo and acousticness, so it cannot "
        "explain whether the user prefers polished dance-pop, aggressive rock, or mellow electronic pop."
    )
    print()
    print("Contrast examples:")
    print(f"Intense rock example: {intense_rock}")
    print(f"Chill lofi example:  {chill_lofi}")
    print()
    print("Improved user profile:")
    print(IMPROVED_USER_PROFILE)
    print()
    print("Why this helps:")
    print(
        "The improved version keeps the main taste signal but adds tempo, acousticness, and valence, "
        "which makes the profile more specific without reducing the user to just one genre and one mood."
    )
    print(
        "Using lists for genres and moods also captures adjacent styles a real listener might enjoy, "
        "so the recommender can prefer upbeat pop and synthy tracks while still rejecting chill lofi "
        "and intense rock when other features do not fit."
    )
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Total songs loaded: {len(songs)}")

    print_profile_review()

    recommendations = recommend_songs(IMPROVED_USER_PROFILE, songs, k=5)
    print(f"Total recommendations: {len(recommendations)}")

    print("\nTop recommendations:\n")
    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]

        print("=" * 48)
        print(f"{index}. {song['title']} by {song['artist']}")
        print(f"Final score: {score:.2f}")
        print("Reasons:")
        for reason in reasons:
            print(f"  - {reason}")
        print()


if __name__ == "__main__":
    main()
