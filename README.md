# What Question Are We Curious to Answer
Are there any NLP models that will parse for US government bill text and categorize the bills content?

# Why We Want to Know
Bill construction is a mystical process.  The Texas 1st District congressman's office does not know how bills come together, how the content is agreed on in committee and how the numbers (dollar figures) in the bills are negotiated.
The congressman's office does not have time to analyze the bills.
This is concerning because the bills result in huge amounts of tax money being extracted from US Citizens.
The goal of this project is to write an analysis tool based on NLP and some of the ideas below.

# NLP Model Types and Training

There are NLP models that can parse and categorize the content of US government bill text. These models can leverage various techniques and tools in natural language processing to analyze legislative documents and classify their content. Here are some approaches and tools that can be used for this task:

1. **Pre-trained Language Models**:
   - **BERT (Bidirectional Encoder Representations from Transformers)**: BERT can be fine-tuned on a labeled dataset of bill texts to classify them into different categories.
   - **GPT (Generative Pre-trained Transformer)**: Similar to BERT, GPT can be used to generate summaries of bill content and can also be fine-tuned for classification tasks.

2. **Text Classification Libraries**:
   - **scikit-learn**: Provides various machine learning algorithms that can be used for text classification after transforming the bill text into numerical features using techniques like TF-IDF.
   - **spaCy**: An industrial-strength NLP library that can be used for text preprocessing, named entity recognition, and can be extended with custom classifiers.
   - **Hugging Face Transformers**: Offers a wide range of pre-trained models, including BERT and GPT, that can be fine-tuned for text classification tasks.

3. **Custom Models**:
   - Developing custom NLP models using deep learning frameworks like TensorFlow or PyTorch. These models can be tailored to the specific characteristics of legislative texts and can be trained on annotated datasets to recognize different categories of bills.

4. **Topic Modeling**:
   - **Latent Dirichlet Allocation (LDA)**: A generative statistical model that can be used to discover the topics present in a collection of documents.
   - **Non-negative Matrix Factorization (NMF)**: Another technique for topic modeling that can be used to understand the underlying themes in bill texts.

5. **Legislative Databases and APIs**:
   - **GovTrack**: Provides access to a comprehensive database of US federal legislation and can be used to obtain bill texts for analysis.
   - **ProPublica Congress API**: Offers access to detailed information about bills, including their texts, which can be used for NLP tasks.

### Example Workflow

1. **Data Collection**: Gather a large dataset of bill texts from sources like GovTrack or the ProPublica Congress API.
2. **Preprocessing**: Clean the text data by removing stop words, punctuation, and other non-informative elements.
3. **Feature Extraction**: Convert the text into numerical features using methods like TF-IDF or word embeddings.
4. **Model Training**: Train a classification model using labeled data. You can use supervised learning techniques and fine-tune pre-trained models like BERT or GPT.
5. **Evaluation**: Evaluate the model's performance using metrics like accuracy, precision, recall, and F1-score.
6. **Deployment**: Deploy the trained model to categorize new bill texts as they become available.

By following these steps and utilizing the appropriate tools and models, you can build an NLP system capable of parsing and categorizing the content of US government bills.


# What You'll Need
1. Python experience
1. access to hugging face repositories for building BERT or GPT model data
1. access to computing resources
1. curiosity


# Researching Data Source

The 2024 congressional spending bills, also known as appropriations bills, are divided into twelve categories that fund various parts of the federal government. Here is the list of the twelve appropriations bills for the fiscal year 2024:

1. **Agriculture, Rural Development, Food and Drug Administration, and Related Agencies**
2. **Commerce, Justice, Science, and Related Agencies**
3. **Defense**
4. **Energy and Water Development, and Related Agencies**
5. **Financial Services and General Government**
6. **Homeland Security**
7. **Interior, Environment, and Related Agencies**
8. **Labor, Health and Human Services, Education, and Related Agencies**
9. **Legislative Branch**
10. **Military Construction, Veterans Affairs, and Related Agencies**
11. **State, Foreign
12. - model stopped answering here (ChatGPT)
   

