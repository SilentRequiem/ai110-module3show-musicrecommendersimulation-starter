# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeMatch 1.0

---

## 2. Intended Use

This recommender suggests 3–5 songs from a small dataset based on a user’s music preferences. It assumes the user has clear preferences for genre, mood, and energy. This system is designed for classroom learning and not for real-world users.

---

## 3. How the Model Works

The model uses a content-based scoring system. It looks at features like genre, mood, energy, tempo, acousticness, and valence. It compares these to a user profile and gives each song a score.

Songs get the most points for matching genres, then mood, and then additional points if their features are close to the user’s preferences. Compared to the starter version, I added more features and allowed multiple genres and moods.

---

## 4. Data

The dataset contains 18 songs in a CSV file. I added more songs to increase variety across genres like pop, rock, ambient, hip-hop, and EDM.

The dataset includes features like energy, tempo, valence, and acousticness. However, it does not include lyrics, artist popularity, or listening history, so it is limited.

---

## 5. Strengths

The system works well for users with clear preferences, like high-energy pop or chill lofi. It captures vibe well using energy and mood.

It also provides explanations, which makes the recommendations easy to understand.

---

## 6. Limitations and Bias

The system can over-prioritize genre, which may cause songs to rank high even if their vibe is not perfect.

The dataset is small, so recommendations can repeat. It also simplifies music taste into a few features, which does not reflect real user behavior.

---

## 7. Evaluation

I tested the system with multiple profiles: high-energy pop, chill lofi, and intense rock.

The results matched expectations. High-energy profiles returned upbeat songs, while chill profiles returned calmer tracks.

I also reduced genre weight as an experiment, which increased variety but sometimes reduced accuracy.

---

## 8. Future Work

- Add more songs for better variety
- Improve balance between features
- Add more features like lyrics or artist similarity
- Increase diversity in recommendations

---

## 9. Personal Reflection

This project showed how simple scoring systems can create realistic recommendations. Small changes in weights or features can have a big impact on results.

It also showed how bias can appear easily, especially with small datasets or unbalanced scoring.
