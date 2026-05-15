# Expert System for Hospital and Medical Facilities
## Artificial Intelligence Practical
## Aim

# Implement an Expert System for hospital and medical facility diagnosis.
# ## Theory

# An Expert System is an AI application that uses knowledge and rules to solve problems like a human expert.

# This expert system provides basic medical suggestions based on symptoms entered by the user.
# Hospital Expert System

print("===== Hospital Expert System =====")

fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()

print("\nDiagnosis Result:")

if fever == "yes" and cough == "yes":
    print("You may have Flu or Viral Infection.")

elif fever == "yes" and headache == "yes":
    print("You may have Fever or Migraine.")

elif cough == "yes":
    print("You may have Throat Infection.")

elif headache == "yes":
    print("You may be stressed or tired.")

else:
    print("You seem healthy.")
## Conclusion

# The Expert System was implemented successfully.
# The system provides simple medical suggestions based on user symptoms using rule-based logic.
