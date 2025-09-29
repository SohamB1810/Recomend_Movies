# 🎬 Movie Recommendation System

## 🚀 Project Overview

Welcome to our Movie Recommendation System, where movie suggestions go beyond the ordinary. This intelligent application blends advanced recommendation strategies, including Collaborative Filtering, Content-Based Recommendation, and Non-Personalized Approaches, to curate a personalized and engaging movie-watching experience.

## 🔍 Problem Statement

Finding the perfect movie can be a challenge, especially for new users. Our system addresses this by seamlessly transitioning from non-personalized recommendations to advanced models. Whether you're a seasoned critic or a first-time viewer, our system adapts to your preferences.


## 🎯 Recommendation Approaches

### A) Simple Recommender System - Average Weight

The Simple Recommender system offers universal movie suggestions by considering overall popularity and occasional genre preferences. This model prioritizes movies with higher popularity and critical acclaim, assuming they are more likely to be appreciated by the average audience.

**Implementation:**
- Movies are sorted based on ratings and popularity.
- Top movies from this sorted list are presented.
- Users can specify a genre for personalized recommendations.

**Mathematical Model (IMDB's Weighted Rating Formula):**

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/28d5a9c1-c5d4-4c85-9455-46ccc9997a31)


- **v:** Number of votes for the movie
- **m:** Minimum votes required to be listed in the chart (set at the 85th percentile)
- **R:** Average rating of the movie
- **C:** Mean vote across the entire dataset

**Functionality:**
- Create Top 250 movies chart.
- Develop charts tailored to specific genres.

### B) Content-Based Recommendation System

Enhance the personalization of recommendations with a Content-Based Recommendation engine. This engine calculates similarities between movies using specific criteria, suggesting movies that closely resemble a particular film enjoyed by the user.

**Focus Areas:**
- Movie Overviews
- Movie Cast
- Director
- Keywords
- Genre

**Working Mechanism:**
- Content-Based Recommendation focuses on intrinsic movie features, such as Movie Cast,Director and genres.
- Understand your preferences through the genres, favourtive cast and the director you enjoy.
- Predict and suggest movies with similar content, adding a layer of personalization based on thematic elements.


## 📊 Key Aspects and Features
- 🤖 **Content-Based Recommendation:** Discover movies similar to your favorites using advanced natural language processing and cosine similarity.
- 👑 **Popularity-Based Recommendation:** Explore trending movies based on overall popularity and user ratings.
- 📊 **Data Analysis:** Dive into insightful visualizations exploring the world of movies, genres, and more.
- 🌐 **Streamlit Web App:** Explore movie recommendations interactively through our Streamlit web app. Tailor your preferences, and witness the system craft a unique movie playlist just for you.

## 🛠️ Technologies and Techniques Used
- 🐍 Python
- 📊 Pandas, NumPy, Matplotlib, Seaborn
- 🤖 Natural Language Processing with NLTK
- 🤖 Machine Learning with Scikit-Learn
- 🌐 Streamlit for Web App Development
- 📡 Requests for HTTP Handling



## 📄 Usage Instructions
**Get Started:**
1. 📥**Clone the repository:**
   ```bash
   git clone https://github.com/Bidishabiswas1704/recomend_movie.git
   ```

2. 🚀**Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. 🌐**Deployment:**
   ```bash
   streamlit run app.py
   ```
   Feel free to explore, contribute, and enhance the movie recommendation experience. Your movie night starts here! 🍿✨
   
5. **Open the web browser and go to [http://localhost:8501](http://localhost:8501) to explore the Movie Recommendation System.**

## 📊 Data Exploration and Analysis (Jupyter Notebook)

### Step 1: Loading Data
- Open the Jupyter Notebook (`Movie_Recommendation_System.ipynb`) to initiate the exploration and analysis of the movie dataset.
- Follow the step-by-step instructions to load the movie data from (`tmdb_5000_movies.csv`) and proceed with the analysis.

### Step 2: Selecting Key Features
- Identify and select key features for the analysis, including genres, id, keywords, overview, popularity, release_date, title, vote_average, vote_count, cast, and crew.

### Step 3: Cleaning Data
- Clean the data, especially focusing on columns like genres, keywords, cast, and crew, which are in dictionary format.
- Utilize the Abstract Syntax Trees (`.ast`) module in Python to convert dictionary literals into objects.
- **Screenshots:**
  - Screenshot of loaded data.

  ![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/cf753c38-c6b5-4775-830d-a71194e8e0b4)

  - Screenshot of selected key features.
 
  ![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/22778c55-dd28-473c-afe0-ac900eb41216)

  - Screenshot of cleaned data.

  ![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/c05de84f-7418-4332-a8f6-7d5ff22512c4)


## A) Recommendation System Based on Average Weight

### Step 4: Calculate Weighted Rating Components
- Implement the calculation of all components of the weighted rating, incorporating factors like vote count, average rating, and overall popularity.

### Step 5: Recommendation Based on Average
- For the recommendation system based on average, focus on specific columns: genre, popularity, release_date, vote_average, vote_count, and weighted_average.

### Step 6: Popularity-Based Recommendation
- Arrange movies in descending order based on popularity to check for popular recommendations.
- **Screenshots:**
  - Screenshot of calculated weighted rating components.

  ![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/fe037613-a2a7-4603-aeb6-cea272eba3ef)

  - Screenshot of recommendations based on average.

  ![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/149bd7e3-efd2-4a54-a39d-816dd5b3731e)

  - Screenshot of popularity-based recommendations.

  ![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/c4c03d17-34d0-42cb-b784-e0ba5e3cefca)


### Step 7: Combined Recommendation System
- Create a new recommendation system that considers both weighted average and popularity with a 50-50 priority, forming a new column as a scorecard.
- **Screenshots:**
  - Screenshot of the combined recommendation system.

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/e00eaecb-2314-4310-bb0e-b8f81a897998)

### Step 8: Genre-Specific Recommendations
- Explore recommendations based on particular genres.
- **Screenshots:**
  - Screenshot of genre-specific recommendations.

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/fa2aa12b-6b60-4932-b624-535e98309b31)

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/cfe2592a-2d31-4174-a650-95267727652e)


## B) Content-Based Recommendation System

### Step 9: Selecting Features for Content-Based Recommendation
- Choose key features for the Content-Based Recommendation System, including id, title, genres, keywords, overview, cast, and director.

### Step 10: Preprocessing Overview
- Split words in the overview into individual tags and create a collection of tags from columns like genres, overview, keywords, cast, and director.
- **Screenshots:**
  - Screenshot of selected features for content-based recommendation.

  ![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/11132bf7-4d08-414d-9bfb-d7e31c3b2030)

  - Screenshot of preprocessing overview.

  ![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/0d138c0e-8938-4ac6-ae52-7f5aaf37982c)


### Step 11: Building Recommendation System
- Convert each tag of a particular movie into a set of arrays and form a matrix.
- Build a recommendation system based on the similarity of arrays by calculating the minimum distance between two pairs.
- **Screenshots:**
  - Screenshot of building the content-based recommendation system.

  ![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/4adcbea4-dbfa-457e-bd06-d32d4882a6fb)


### Step 12: Customizing Recommendations
- Replace 'particular movie' with the desired movie title to tailor recommendations according to user preferences.

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/34eb8268-b178-4916-af00-9436da25de34)

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/c71e1f2a-40e6-4d19-9568-b818b9d42a5c)



Explore the notebook for a detailed walkthrough of these steps and gain insights into the world of movie recommendations!

## 📊 Example Screenshots and User Guidance (Streamlit Web App)

### Step 1: Opening the Streamlit Web App Interface

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/26f6aade-5b9d-4630-ab60-88fc70bb643a)

- Open the Streamlit web app interface by running the provided command in the terminal.
- The initial screen presents a clean and user-friendly interface.

### Step 2: Choosing Recommendation Approaches

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/525d56b2-9fb4-488e-9aeb-c8895d893a08)

- Select the recommendation approaches you would like to explore.

### Step 3a: Popularity-Based Recommendation System

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/c24ecd91-5ee7-4364-af88-89c7c31317a7)

- Navigate to the popularity-based recommendation system.
- A new interface appears with the same heading.

### Step 4: Choosing Genres for Recommendations

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/708ecfd8-0b3e-48c7-8a20-7bfac31dcf3e)

- Choose the genres of your interest.
- The system will suggest 250 movies with their posters in descending order of the scorecard within the selected genres.
- **Screenshot:**
  - Screenshot of the popularity-based recommendation system.

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/94174385-51df-46fe-8a44-dc963a7f82e3)

### Step 3b: Content-Based Recommendation System

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/ba793621-5f7c-49cd-834c-4ea62fee3df8)

- Switch to the content-based recommendation system in the select box.

### Step 5: Typing Movie Title for Recommendations

- Type the title of a movie, and the system will show 5 similar movie names with their posters.

![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/a1a82086-b064-4c4b-a1b5-eceb785641a8)

- **Screenshot:**
  - Screenshot of the content-based recommendation system.
  
![image](https://github.com/Bidishabiswas1704/recomend_movie/assets/140384850/fe71e578-0e0c-43d5-8cef-1a6813d20e1b)

### Recruiters and Users Note:
- As a recruiter or user, this intuitive interface allows for easy navigation and a seamless experience.
- Explore the power of different recommendation approaches with just a few clicks!
- Screenshots strategically placed after each step for visual validation and guidance.

## 📂 Directory Structure

```
.
├── data/
│   └── tmdb_5000_movies.csv
├── notebooks/
│   └── Movie_Recommendation_System.ipynb
├── screenshots/
│   ├── screenshot1.png
│   └── screenshot2.png
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── .github/
    
```

## 🤝 Contribution

Contributions are more than welcome! Feel free to open issues, propose new features, or submit pull requests to enhance the Movie Recommendation System.

## Authors

- [@Bidisha_Biswas](https://www.github.com/Bidishabiswas1704)


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy an immersive movie experience tailored just for you!
