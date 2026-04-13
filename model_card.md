# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

One limitation of this system is that it can over-prioritize certain features, especially genre. This can cause songs with the correct label to rank higher even if their overall vibe is not the best match.

Another issue is that the dataset is small, so some genres and moods are underrepresented. This can lead to repeated recommendations and less diversity.

The system also assumes all users can be described using a few numerical features like energy and valence, which oversimplifies real music taste. This could make the system less fair or accurate for users with more complex preferences.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I tested the recommender using multiple user profiles, including high-energy pop, chill lofi, and intense rock. I compared the top results for each profile to see if they matched the expected vibe.

The results generally made sense. High-energy profiles returned upbeat songs, while low-energy profiles returned calmer tracks. However, some songs appeared across multiple profiles, showing that shared features like energy and valence can influence results across different tastes.

I also tested a change to the scoring system by lowering the importance of genre. This increased diversity but sometimes reduced accuracy for users with strong genre preferences.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
