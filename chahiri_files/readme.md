In this project, I tried to combine the technologies that I except we will use in the future.:

1. **ChromaDB**: to retrieve therapeutic conversations and associated emotions from the "psychotherapy" dataset on hugging face.

2. **LLM Integration**: I used gemini flash 2.0

3. **Emotion-Aware Response Generation**: The assistant analyzes user input, identifies emotional states, and retrieves relevant therapeutic conversations from the ChromaDB database to inform its responses.

4. **Red Flag Detection**: To identify potentially serious mental health concerns (like self-harm or suicidal ideation) by comparing detected emotions against a predefined set of red flags.

5. **Custom Agent Architecture**: to give therapeutic advice.

The system first processes user input to extract emotional context, queries the database for relevant therapeutic conversations, checks for potential red flags, and then generates an empathetic response using the LLM that incorporates both the detected emotion and appropriate therapeutic language. This creates a supportive conversational experience informed by professional therapeutic approaches.



**To do**: Working on optimizing the code and adding more features.