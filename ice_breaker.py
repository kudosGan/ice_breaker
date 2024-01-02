import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


information = """ Yoshua Bengio OC FRS FRSC (born March 5, 1964[3]) is a Canadian computer scientist, most noted for his work on artificial neural networks and deep learning.[4][5][6] He is a professor at the Department of Computer Science and Operations Research at the Université de Montréal and scientific director of the Montreal Institute for Learning Algorithms (MILA).[1]

Bengio received the 2018 ACM A.M. Turing Award (often referred to as the "Nobel Prize of Computing"), together with Geoffrey Hinton and Yann LeCun, for their work on deep learning.[7] Bengio, Hinton, and LeCun are sometimes referred to as the "Godfathers of AI" and "Godfathers of Deep Learning".[8][9][10][11][12][13] As of May 2023, he has the highest h-index of any computer scientist.[14]

Early life and education
Bengio was born in France to a Jewish family who immigrated to France from Morocco, and then immigrated again to Canada.[15] He received his Bachelor of Science degree (electrical engineering), MSc (computer science) and PhD (computer science) from McGill University.[2][16]

Bengio is the brother of Samy Bengio,[15] also an influential computer scientist working with neural networks, who is currently Senior Director of AI and ML Research at Apple.

The Bengio brothers lived in Morocco for a year during their father's military service there.[15] His father, Carlo Bengio, was a pharmacist who wrote theatre pieces and ran a Sephardic theatrical troupe in Montreal that played Judeo-Arabic pieces.[17][18] His mother, Célia Moreno, is also an artist who played in one of the major theatre scenes of Morocco that was run by Tayeb Seddiki in the 1970s.[19]

Career and research
After his PhD, Bengio was a postdoctoral fellow at MIT (supervised by Michael I. Jordan) and AT&T Bell Labs.[20] Bengio has been a faculty member at the Université de Montréal since 1993, heads the MILA (Montreal Institute for Learning Algorithms) and is co-director of the Learning in Machines & Brains program at the Canadian Institute for Advanced Research.[16][20]

Along with Geoffrey Hinton and Yann LeCun, Bengio is considered by journalist Cade Metz to be one of the three people most responsible for the advancement of deep learning during the 1990s and 2000s.[21] Among the computer scientists with an h-index of at least 100, Bengio was as of 2018 the one with the most recent citations per day, according to MILA.[22][23] As of December 2022, he had the 2nd highest Discipline H-index (D-index) in computer science.[24] Thanks to a 2019 article on a novel RNN architecture, Bengio has an Erdős number of 3.[25]

In October 2016, Bengio co-founded Element AI, a Montreal-based artificial intelligence incubator that turns AI research into real-world business applications.[21] The company sold its operations to ServiceNow in November 2020,[26] with Bengio remaining at ServiceNow as an advisor.[27][28]

Bengio currently serves as scientific and technical advisor for Recursion Pharmaceuticals[29] and scientific advisor for Valence Discovery.[30]

Views on AI
Following concerns raised by AI experts about the existential risks AI poses on humanity, in May 2023, Bengio stated in an interview to BBC that he felt "lost" over his life's work. He raised his concern about "bad actors" getting hold of AI, especially as it becomes more sophisticated and powerful. He called for better regulation, product registration, ethical training, and more involvement from governments in tracking and auditing AI products. [31][32]

Speaking with the Financial Times also in May 2023, Bengio said that he supported the monitoring of access to AI systems such as ChatGPT so that potentially illegal or dangerous uses could be tracked.[33]


"""




if __name__=='__main__':
    
    print("hello Langchain!")

    summary_template = """
            give the Linkedin information {information} abnotu  a person from  I want you to Create:
            1.  as short summary
            2. two intersting facts about them
            3.  what is his last name  from  which country
            4. Date of Birth 


"""
 
summary_prompt_template = PromptTemplate(input_variables=[information], template=summary_template)


llm =ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")


chain = LLMChain(llm=llm, prompt=summary_prompt_template)


print(chain.run(information = information))