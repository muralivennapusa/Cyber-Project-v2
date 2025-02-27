import streamlit as st

def Home():
    import streamlit as st

    st.markdown('''<h1 style='text-align:left;font-size:60px;'>👮Tamil Nadu Police👮</h1>\n\n\n\n
                ''', unsafe_allow_html=True)

    st.write("# Welcome dear Officer! 🫡")
    st.title("To the Cyber Crime Assistance Portal")
    st.markdown(
        """
            ## What would you like to do today?
    
    - 🚨 **Classify a Cyber Crime:** 
    Use AI-powered NLP to categorize a cyber crime incident.
    
    - 📊 **View Cyber Crime Statistics:** 
    See trends and reports on cyber attacks by hacktivist groups.
    
    - 📁 **View Uploaded Evidence:** 
    Examine supporting documents or media related to a witnessed cyber crime that are uploaded by citizens.
    
    - 📚  **Forum Monitoring:** 
    Monitor the IT Act and DPDP Act in discussion forums.

    
    """
    )
    st.write("\n\nNavigate around our portal to use the above services. It's our job to make the society better." )   


def Uploaded_Files():
    import os
    import streamlit as st
    import pandas as pd
#    import fitz  # PyMuPDF for PDF reading
    from PIL import Image

    # Directory containing files
    path = "./dump"

    # Ensure the directory exists
    if not os.path.exists(path):
        st.error(f"Directory '{path}' not found!")
    else:
        dir_list = os.listdir(path)

        st.markdown("## 📂 Uploaded Files in Directory:\n")

        for file in dir_list:
            st.write("-",file)


        

def Cyber_Case_Statistics():
    
    import streamlit as st
    import pandas as pd
    import altair as alt

    st.title("Cyber Crimes by Hacktivists over the years!")

    def get_cybercrime_data():
        df = pd.read_csv("stats/cyber_crime_stats.csv")
        return df.set_index("Hacktivist Group")

    try:
        df = get_cybercrime_data()
        groups = st.multiselect(
            "Choose Hacktivist Groups", list(df.index), ["Anonymous", "Lizard Squad","LulzSec","AnonSec","Cracka with Attitude"]
        )
        if not groups:
            st.error("Please select at least one hacktivist group.")
        else:
            data = df.loc[groups]
            st.write("### Cyber Crime Activity (Attack Count)", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Attack Count"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="year:T",
                    y=alt.Y("Attack Count:Q", stack=None),
                    color="Hacktivist Group:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except Exception as e:
        st.error(f"Error loading data: {e}")

def Case_Classifier():
    import streamlit as st
    import time
    # with st.spinner(text="In progress...", show_time=False):
    #     time.sleep(1)
    st.title(" NLP Case Classifier! ")


    
    system_prompt = "You are a cyber case classifier consultant. Be descriptive and helpful."

    response = '''
The penalties and jail time for possession or use of tools or software intended for cybercrime can vary significantly depending on the jurisdiction, the specific nature of the offense, and the intent behind the possession or use of such tools. Here’s a breakdown of some key factors that influence the legal repercussions:

### 1. **Jurisdiction**
   - **United States**: Under the Computer Fraud and Abuse Act (CFAA), penalties can range from fines to several years of imprisonment. For instance, using a computer to commit fraud can lead to up to 10 years in prison for a first offense, and up to 20 years for subsequent offenses.
   - **European Union**: The Directive on attacks against information systems (2013/40/EU) encourages member states to impose effective, proportionate, and dissuasive penalties, which can include imprisonment for several years depending on the severity of the offense.
   - **Other Countries**: Laws vary widely. Some countries may have strict anti-hacking laws with severe penalties, while others may adopt a more lenient approach.

### 2. **Nature of the Offense**
   - **Possession vs. Intent to Use**: Simply possessing tools or software associated with cybercrime may carry lesser penalties than if there is evidence of intent to use them for illegal activities. Intent can be demonstrated through actions such as planning a cyber attack or distributing malware.
   - **Type of Tools**: Certain tools, like malware, ransomware, or hacking software, may carry heavier penalties than more benign tools that could be used for legitimate purposes (e.g., penetration testing tools).

### 3. **Public Interest Litigation (PIL)**
   - In some jurisdictions, public interest litigation may play a role in how cybercrime laws are enforced. If an individual is using software or tools for a legitimate purpose that serves the public interest (e.g., ethical hacking for security assessments), they may be protected under specific laws.
   - However, if the tools are used in a way that breaches laws (even if intended for public good), there could still be legal consequences. Courts may consider the intent and outcome of such actions.

### 4. **Aggravating Factors**
   - **Severity of Harm**: If the possession or use of the tools resulted in significant harm, such as data breaches affecting many individuals or organizations, penalties could be more severe.
   - **Repeat Offenders**: Repeat offenders typically face harsher penalties, including longer prison sentences.
   - **Organization Involvement**
   '''

    st.info("### **User:**")
    input= st.text_input("Case Description", "--------------------------------------------------------")
    user_prompt = input
    with open("stats/promptHistory.txt",'a') as history:
      history.write(user_prompt + "\n")
      history.write("--------------------------------------------------------\n")
    st.write(user_prompt)
    st.error("### **AI:**")
    st.write(response)

def forums():
    import streamlit as st
    
    st.title("Cyber Laws Discussion Forums!")
    st.success("## **Information Technology (IT) Act,2000**")
    st.markdown('''

## Overview
The Information Technology (IT) Act, 2000, is a law in India that primarily deals with cybercrime and electronic commerce. It provides legal recognition to electronic documents and digital signatures.

## Key Provisions
1. **Legal Recognition of Electronic Documents**: Ensures that electronic records and digital signatures are legally valid.
2. **Cyber Crimes and Penalties**:
   - Hacking and unauthorized access.
   - Identity theft and phishing.
   - Cyber terrorism.
   - Publishing or transmitting obscene content.
3. **Regulation of Certifying Authorities**: Establishes guidelines for issuing digital signatures.
4. **Data Protection and Privacy**: Specifies the responsibilities of organizations handling sensitive personal data.
5. **Liabilities of Intermediaries**: Defines the responsibilities of internet service providers and website hosts in preventing cybercrimes.

## Notable Sections and Penalties
- **Section 66A**: Punishment for sending offensive messages through communication service.
  - **Penalty**: Up to 3 years imprisonment and a fine.
- **Section 66B**: Punishment for dishonestly receiving stolen computer resources or communication devices.
  - **Penalty**: Up to 3 years imprisonment and/or a fine of ₹1 lakh.
- **Section 66C**: Identity theft (fraudulent use of digital signatures, passwords, etc.).
  - **Penalty**: Up to 3 years imprisonment and a fine of ₹1 lakh.
- **Section 66D**: Cheating by personation using computer resources (cyber fraud).
  - **Penalty**: Up to 3 years imprisonment and a fine of ₹1 lakh.
- **Section 66E**: Violation of privacy (capturing, publishing private images of others without consent).
  - **Penalty**: Up to 3 years imprisonment and a fine of ₹2 lakh.
- **Section 67**: Publishing obscene material in electronic form.
  - **Penalty**: First conviction - Up to 5 years imprisonment and a fine of ₹10 lakh; subsequent conviction - Up to 10 years imprisonment and a fine of ₹10 lakh.
- **Section 67A**: Publishing sexually explicit content.
  - **Penalty**: First conviction - Up to 5 years imprisonment and a fine of ₹10 lakh; subsequent conviction - Up to 7 years imprisonment and a fine of ₹10 lakh.
- **Section 67B**: Child pornography (publishing or transmitting material depicting children in sexually explicit acts).
  - **Penalty**: First conviction - Up to 5 years imprisonment and a fine of ₹10 lakh; subsequent conviction - Up to 7 years imprisonment and a fine of ₹10 lakh.
- **Section 69**: Government's power to intercept, monitor, or decrypt information in the interest of national security.
  - **Penalty for non-compliance**: Up to 7 years imprisonment and a fine.

## Amendments
- The IT Act was amended in 2008 to include provisions for cyber terrorism and stricter penalties for data breaches.

---
''')
    
    st.success("## **Digital Personal Data Protection (DPDP) Act, 2023**")

    st.markdown('''
## Overview
The DPDP Act, 2023, is India’s comprehensive data protection law aimed at regulating the processing of personal data.

## Key Provisions
1. **Applicability**:
   - Applies to personal data collected, processed, and stored digitally in India.
   - Covers entities that process personal data of Indian citizens, even if they are based outside India.
2. **Consent-Based Data Processing**:
   - Requires clear and explicit consent from individuals before collecting and processing their data.
   - Users have the right to withdraw consent at any time.
3. **Rights of Data Principals**:
   - Right to access, correct, and erase personal data.
   - Right to grievance redressal and data portability.
4. **Obligations of Data Fiduciaries**:
   - Must implement security safeguards to protect personal data.
   - Notify users and authorities in case of data breaches.
5. **Data Protection Board**:
   - A regulatory body established to oversee compliance and handle grievances.
6. **Penalties for Non-Compliance**:
   - Heavy fines for mishandling personal data.
   - Legal action against entities violating data protection norms.

## Notable Sections and Penalties
- **Section 3**: Defines personal data and data principals.
- **Section 7**: Rights of data principals (access, correction, erasure, grievance redressal).
- **Section 8**: Obligations of data fiduciaries (security, purpose limitation, consent management).
- **Section 16**: Data breach notification requirement.
  - **Penalty**: Up to ₹250 crore for non-compliance.
- **Section 25**: Failure to implement security safeguards.
  - **Penalty**: Up to ₹200 crore.
- **Section 29**: Processing children’s data without consent.
  - **Penalty**: Up to ₹100 crore.
- **Section 33**: Non-compliance with directives of the Data Protection Board.
  - **Penalty**: Up to ₹150 crore.

## Significance
- Strengthens privacy rights of individuals.
- Establishes accountability for companies handling personal data.
- Aligns India’s data protection framework with global standards.

---

## 
The IT Act, 2000, and DPDP Act, 2023, together form the legal backbone for cyber regulation and data protection in India. While the IT Act addresses cybercrime and electronic transactions, the DPDP Act focuses on personal data privacy and security.
''')
    
def Prompt_History():
    import streamlit as st
    
    st.title("Prompt History🕣")
    file=open("stats/promptHistory.txt",'r')
    l=[]
    for i in file.readlines():
        l.append(str(i))
    for i in range(len(l)-1):
        if "--------------------------------------" in l[i] and "--------------------------------------" in l[i+1]:
            continue
        st.markdown(str(l[i])+'\n')

page_names_to_funcs = {
    "Uploaded Files": Uploaded_Files,
    "Home": Home,
    "Case Classifier":Case_Classifier,
    "Cyber Cases Statistics": Cyber_Case_Statistics,
    "Prompt History": Prompt_History,
    "Forums":forums,
}

st.sidebar.image(r".\stats\tnp.png")
demo_name = st.sidebar.selectbox("What you want to do?", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
