import pandas as pd
from Project_data import data
class PatientRecords:
    def  __init__(self):
        self.mypd=None

    def project_welcome(self):
        print("===========================================================================================")
        print("🏥 Hospital Patient Records System 📁\n🚀 Built with Python and Pandas to organize, analyze, and manage patient data smartly!\n📊 Power of Data | ❤️ Care with Code")
        print("===========================================================================================")

    def creating_data_frame(self,patient_data):
        try:            
            print("----------------------------------------------------")
            print("✅ DataFrame has been successfully created.")  
            self.mypd=pd.DataFrame(patient_data)
        except Exception as e:
             print("ERROR : ",e)    

    def saving_data_into_csv(self):
        print("CSV file has been created and data saved successfully.")
        self.mypd.to_csv("PatientRecords.csv",index=False)
        print("-------------------------------------------------------")

    def project_req(self):
        print("""
📌 Project: Hospital Patient Records System
This project follows 5 essential steps for effective data handling:

🔹 Step 1: Load and Explore the Dataset  
🔹 Step 2: Clean and Analyze Missing Data  
🔹 Step 3: Data Manipulation and Transformation  
🔹 Step 4: Interpolation and Data Completion  
🔹 Step 5: Save the Cleaned Data to CSV 📁

🧠 Developed using Python and Pandas  
👨‍💻 By: Junaid Mustafa — 1st Year Software Engineering Student  
🎯 Aspiring Future AI Engineer
""")
    def step1(self):
            print("""
--------------------------------------------------------------                  
🔹 Step 1: Load and Explore the Dataset
--------------------------------------------------------------    
1. Load the dataset using `pd.read_csv()`
2. Show the top 3 and bottom 2 records using `.head()` and `.tail()`
3. Display the number of rows and columns using `.shape`
4. Show all column names using `.columns`
5. Use `.info()` to check data types and missing values
--------------------------------------------------------------                      
""")
    def load_Dataset(self):
         try: 
            print("--------------------------------------------------------------------------------------------") 
            print("DATA SET HAS BEEN LOADED")
            print("--------------------------------------------------------------------------------------------") 
            self.mypd=pd.read_csv("PatientRecords.csv")
            print(self.mypd)
            print("--------------------------------------------------------------------------------------------") 
         except Exception as e:
              print("ERROR : ",e)

    def show_rows(self):
            try:
                print("--------------------------------------------------------------------------------------------") 
                print("SHOWING TOP THREE ROWS :")
                print(self.mypd.head(3))
                print("--------------------------------------------------------------------------------------------")
                print("SHOWING LAST TWO ROWWS :")
                print(self.mypd.tail(2))
                print("--------------------------------------------------------------------------------------------")
            except Exception as e:
                 print("ERROR : ",e)    

    def displaying_no_rows(self):
         try:
              print("-------------------------")
              print("TOTAL ROWS AND COLUMNS")  
              print("------------------------") 
              print(self.mypd.shape)
              print("------------------------") 
         except Exception as e:
              print("ERROR : ",e)

    def showing_columns(self):
          try:  
            print("-------------------------")
            print("COLUMNS:")
            print("-------------------------")
            print(self.mypd.columns)
            print("-------------------------")
          except Exception as e:
               print("ERROR : ",e)


    def sumary_info(self):
         try:
              print("------------------------------------------------")
              print("SUMARY INFO OF DATA FRAME IS : ")
              print("------------------------------------------------")
              print(self.mypd.info())
              print("------------------------------------------------")
         except Exception as e:
              print("ERROR : ",e)     


    def step2(self):
        print("""
--------------------------------------------------------------                  
🔹 Step 2: Clean and Analyze Missing Data
--------------------------------------------------------------    
6. Use `.isnull()` to find missing values
7. Use `.dropna()` to drop rows with missing Diagnosis and Charges
8. Use `.fillna()` to:
   - Fill missing 'Medicine' with "To be Prescribed"
   - Fill missing 'Charges' with 0
--------------------------------------------------------------                  
""")
        
    def missing_value(self):
         print("---------------------------------")
         print("MISSING VALUE : ")
         print("---------------------------------------")
         print(self.mypd.isnull())
         print("---------------------------------------")

    def droping_specfic_rows(self):
         print("---------------------------------------------------")
         print("DATA FRAME BEFORE REMOVING")
         print("---------------------------------------------------")
         print(self.mypd)
         print("---------------------------------------------------")
         print("HERE WE REMOVED MULTIPLE COLUMNS")
         print("---------------------------------------------------")
         self.mypd.drop(columns=["Diagnosis","Charges"],inplace=True)
         print("AFTER DROPING!")
         print(self.mypd)
         print("---------------------------------------------------")

    def filling_missing_data(self):
         self.mypd['Medicine']=self.mypd['Medicine'].fillna("To be Prescribed")
         print("----------------------------------------------------------------")
         print("FILLING MISSING MEDICINE : ")
         print(self.mypd)
         print("----------------------------------------------------------------")
         print("FIILLING MISSING CHARGES VALUES WITH 0 : ")
         print("----------------------------------------------------------------")
         self.mypd['Charges']=self.mypd['Charges'].fillna(0)
         print(self.mypd)     

    def step3(self):
        print("""
--------------------------------------------------------------                  
🔹 Step 3: Data Manipulation
--------------------------------------------------------------    
9. Use `.insert()` to add a new column called 'Hospital' with the value 'City Hospital' for all patients
10. Use `.loc[]` to:
    - Display data for all patients whose Status is 'Admitted'
    - Update the Status of PatientID 2 to 'Recovered' using `.loc[]`
--------------------------------------------------------------    
""")        
    def adding_column(self):
            print("----------------------------------------------------------------")
            print("ADDING COLUMN AFTER THE VIEW OF DATA FRAME IS : ")
            self.mypd.insert(8,"Hospital",'City Hospital')
            print(self.mypd) 
            print("----------------------------------------------------------------")
             
    def using_loc(self):
         print("-----------------------------------------------------------") 
         print("DISPLAYING DATA FOR ALL PATIENTS WHO STATUS IS 'Admitted")
         print("-----------------------------------------------------------")
         filter = self.mypd[self.mypd['Status']=='Admitted']
         print(filter)
         print("-----------------------------------------------------------")
         print("UPDATING THE STUTUS OF PAITENT 2 : ")
         self.mypd.loc[2,"Status"]='Recovered'
         print(self.mypd.head(3))
         print("------------------------------------------------------------")
            

    def step4(self):
            print("""
--------------------------------------------------------------                      
🔹 Step 4: Interpolation
--------------------------------------------------------------    
11. Assume a column 'Temperature' is added:
    df['Temperature'] = [98.5, np.nan, 99.1, 100.2, np.nan]

    Use `.interpolate()` to fill missing temperature values

--------------------------------------------------------------    
""")
    def adding_ass_column(self):
         print("------------------------------------------------------------")
         print("ADDING TEMPERATURE COLUMN  : ")
         print("-----------------------------------------------------------")
         self.mypd.insert(8,"Temperature",[98.5, None, 99.1, 100.2, None])
         print(self.mypd)
         print("-----------------------------------------------------------")
         print("FILLING MISSING TEMPERATURE")
         self.mypd["Temperature"]=self.mypd["Temperature"].interpolate(method="linear")
         print(self.mypd)
         print("-------------------------------------------------------------------------")   

    def step5(self):
            print("""
--------------------------------------------------------------                      
🔹 Step 5: Save the Cleaned Data
--------------------------------------------------------------    
12. Save your final cleaned dataset to a new file called 'cleaned_patients.csv'
    Use `.to_csv('cleaned_patients.csv', index=False)` to save without the index
--------------------------------------------------------------    
""")

    def cleaned_data(self):
            self.mypd['Charges']=self.mypd['Charges'].fillna(0)
            self.mypd['Medicine']=self.mypd['Medicine'].fillna("To be Prescribed")
            self.mypd.to_csv("cleaned_patients.csv",index=False)
            print("---------------------------------------------------")  
            print("DATA HAS BEEN SAVED")
            print("---------------------------------------------------")  
            print(self.mypd)      

records=PatientRecords()
records.project_welcome()
records.creating_data_frame(data)
records.saving_data_into_csv()
while True:
    records.project_req()
    try:
        choice = int(input("👉 Select an option from 1 to 5: "))
        if choice == 1:
            records.step1()
            try:
                select = int(input("👉 Select an option from 1 to 5: "))
                if select == 1:
                    records.load_Dataset()
                elif select ==2:
                    records.show_rows()
                elif select ==3:
                    records.displaying_no_rows()
                elif select ==4:
                    records.showing_columns()
                elif select ==5:
                    records.sumary_info()
                else:
                    print("❗ Invalid input. Choose a number from 1 to 5 only.")
            except ValueError as e:
                 print("ERROR : ",e)        
                
        elif choice == 2:
            records.step2()
            try:
                select = int(input("👉 Select an option from 6 to 8: "))
                if select ==6:
                    records.missing_value()
                elif select ==7:
                    records.droping_specfic_rows()    
                elif select ==8:
                    records.filling_missing_data()  
                else:
                    print("❗ Invalid input. Choose a number from 6 to 8 only.")
            except ValueError as e:
                 print("ERROR : ",e)

        elif choice == 3:
            records.step3()
            try:
                select = int(input("👉 Select an option from 9 to 10: "))
                if select==9:
                     records.adding_column()
                elif select ==10:
                     records.using_loc()
                else:
                     pass
            except ValueError as e:
                 print("ERROR : ",e)    

        elif choice == 4:
            records.step4()
            try:
                select = int(input("👉 ENTER 11 TO SEE FUNCTION : "))
                if select==11:
                     records.adding_ass_column()
                else:
                       print("❌INVALID INPUT")   
            except ValueError as e:
                 print("ERROR : ",e)     
                     
        elif choice ==5:
            records.step5()
            try:
                select = int(input("👉 ENTER 12  TO SAVE CLEAN DATA : "))
                if select==12:
                     records.cleaned_data()         
                else:
                     print("❌INVALID INPUT") 
            except ValueError as e:
                 print("ERROR : ",e  )         
        else:
            print("❗ Invalid input. Choose a number from 1 to 5 only.")
    except ValueError as e:
        print("ERROR : ",e)

    again = input("DO YOU WANT TO CONTINUE (YES/NO) : ").strip().lower()
    if again=="yes":
         continue
    elif again=="no":
        print("--------------------------------------------------")
        print("🎉 Project Completed Successfully! We hope it helped you understand Python + Pandas better. Keep coding and stay curious! 💻📊")
        print("--------------------------------------------------")
        break
    else:
         print("❗ Invalid input")
         break
             




