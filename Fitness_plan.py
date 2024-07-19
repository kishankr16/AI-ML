import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# Function to generate a personalized fitness plan
def generate_fitness_plan(age, weight, fitness_goal, gender):
    plan = ""
    
    if fitness_goal == "Lose Weight":
        plan += "### Fitness Plan to Lose Weight\n"
        plan += "1. **Cardio exercises**: Engage in cardio exercises like running, cycling, or swimming for at least 30 minutes, 5 times a week.\n"
        plan += "2. **Strength training**: Include strength training exercises 3 times a week to build muscle and boost metabolism.\n"
        plan += "3. **Diet**: Maintain a calorie deficit diet by reducing calorie intake and choosing nutrient-dense foods.\n"
        plan += "4. **Hydration**: Drink plenty of water throughout the day.\n"
        plan += "5. **Sleep**: Ensure 7-9 hours of quality sleep each night.\n"
        plan += "6. **Consistency**: Stay consistent and track your progress.\n"
        
    elif fitness_goal == "Build Muscle":
        plan += "### Fitness Plan to Build Muscle\n"
        plan += "1. **Strength training**: Focus on weight lifting and resistance training 4-5 times a week, targeting different muscle groups each session.\n"
        plan += "2. **Compound movements**: Include exercises like squats, deadlifts, and bench presses.\n"
        plan += "3. **Diet**: Consume a protein-rich diet with a slight calorie surplus to support muscle growth.\n"
        plan += "4. **Recovery**: Ensure adequate rest and recovery between workouts.\n"
        plan += "5. **Supplements**: Consider supplements like whey protein and creatine, if needed.\n"
        plan += "6. **Hydration**: Drink plenty of water to stay hydrated.\n"
        
    elif fitness_goal == "Maintain Fitness":
        plan += "### Fitness Plan to Maintain Fitness\n"
        plan += "1. **Balanced routine**: Mix cardio and strength training exercises 3-4 times a week.\n"
        plan += "2. **Flexibility**: Include stretching and flexibility exercises to improve range of motion.\n"
        plan += "3. **Diet**: Maintain a balanced diet to support your current fitness level.\n"
        plan += "4. **Hydration**: Drink enough water daily.\n"
        plan += "5. **Sleep**: Ensure adequate sleep each night.\n"
        plan += "6. **Consistency**: Keep a consistent workout schedule.\n"
    
    # Customize based on age and weight
    if age > 50:
        plan += "\n### Additional Notes for Seniors\n"
        plan += "1. **Low-impact exercises**: Include low-impact cardio exercises like walking or swimming to reduce joint stress.\n"
        plan += "2. **Flexibility and balance**: Focus on exercises that improve flexibility and balance, such as yoga or tai chi.\n"
        plan += "3. **Strength training**: Use lighter weights and more repetitions.\n"
        plan += "4. **Consultation**: Consult with a healthcare provider before starting any new exercise program.\n"
    if weight > 100:
        plan += "\n### Additional Notes for Higher Weight\n"
        plan += "1. **Low-impact cardio**: Start with low-impact cardio exercises like walking or water aerobics to minimize joint stress.\n"
        plan += "2. **Gradual progression**: Gradually increase the intensity and duration of workouts.\n"
        plan += "3. **Supportive footwear**: Wear supportive shoes to protect your joints during exercise.\n"
        plan += "4. **Diet**: Work with a nutritionist to develop a sustainable and balanced diet plan.\n"

    # Gender-based suggestions
    if gender == "Male":
        plan += "\n### Suggestions for Males\n"
        plan += "1. **Strength Focus**: Incorporate strength training with compound movements for overall muscle gain.\n"
        plan += "2. **Protein Intake**: Ensure adequate protein intake to support muscle repair and growth.\n"
        plan += "3. **Cardio and Strength Balance**: Combine cardio with strength training for optimal fitness.\n"
    elif gender == "Female":
        plan += "\n### Suggestions for Females\n"
        plan += "1. **Balanced Routine**: Mix cardio with strength training to tone muscles and improve endurance.\n"
        plan += "2. **Core and Lower Body**: Focus on exercises targeting core strength and lower body.\n"
        plan += "3. **Flexibility and Balance**: Include flexibility exercises like yoga for overall well-being.\n"

    return plan

# Function to generate QR code from text
def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    return img_bytes

# Title of the app
st.title("Personalized Fitness Plan Generator")

# User inputs
age = st.number_input("Enter your age:", min_value=1, max_value=120, value=25)
weight = st.number_input("Enter your weight (in kg):", min_value=1, max_value=200, value=70)
fitness_goal = st.selectbox("Select your fitness goal:", ["Lose Weight", "Build Muscle", "Maintain Fitness"])
gender = st.selectbox("Select your gender:", ["Male", "Female"])

# Generate fitness plan button
if st.button("Generate Fitness Plan"):
    plan = generate_fitness_plan(age, weight, fitness_goal, gender)
    st.markdown(plan)

    # Generate QR code for the fitness plan
    qr_code = generate_qr_code(plan)
    st.image(qr_code, caption="QR Code for Your Fitness Plan", use_column_width=True)

    # Option to download the QR code
    st.download_button(
        label="Download QR Code",
        data=qr_code,
        file_name="fitness_plan_qr_code.png",
        mime="image/png",
    )
