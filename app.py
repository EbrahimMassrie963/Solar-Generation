# app.py
import streamlit as st
from model_utils import predict_energy

def main():
    # Page configuration and styling
    st.set_page_config(
        page_title="Solar Energy Predictor",
        page_icon="☀️",
        layout="wide"
    )

    # Custom CSS styling
    st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stTitle {
            color: #1E88E5;
            font-size: 3rem !important;
            padding-bottom: 2rem;
        }
        .description {
            background-color: #f0f2f6;
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .prediction-box {
            background-color: #e3f2fd;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            margin-top: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Application header with icon
    st.title("☀️ Solar Energy Production Predictor")

    # Enhanced description with better formatting
    with st.container():
        st.markdown("""
        <div class="description">
            <h4>Welcome to the Solar Energy Prediction System</h4>
            <p>Our advanced machine learning model helps you predict solar energy production 
            by analyzing key environmental factors. Simply input the ambient temperature 
            and solar irradiance measurements to get accurate power output predictions.</p>
        </div>
        """, unsafe_allow_html=True)

    # Input section with improved layout
    st.subheader("📊 Input Parameters")
    
    # Create three columns for better spacing
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        Amb_Temp = st.number_input(
            "🌡️ Ambient Temperature (°C)",
            min_value=-10.0,
            max_value=35.0,
            value=25.0,
            step=0.1,
            format="%.6f",
            help="Enter the ambient temperature in degrees Celsius"
        )
    
    with col2:
        radiation = st.number_input(
            "☀️ Solar Irradiance (W/m²)",
            min_value=0.0,
            max_value=2000.0,
            value=800.0,
            step=0.1,
            format="%.6f",
            help="Enter the solar irradiance in watts per square meter"
        )

    with col3:
        model_choice = st.selectbox(
            "🤖 Select Model",
            ["Gradient Boosting Regressor", "Linear Regression"],
            help="Choose the prediction model to use"
        )
        predict_button = st.button("🔮 Generate Prediction", use_container_width=True)

    # Prediction section
    if predict_button:
        with st.spinner('Calculating prediction...'):
            # Get predictions from selected model
            predictions = predict_energy(Amb_Temp, radiation, model_choice)
            
            # Display only the selected model's prediction with an enhanced layout
            st.markdown(f"""
                <div class="prediction-box" style="max-width: 600px; margin: 2rem auto;">
                    <h3 style="color: #1E88E5; margin-bottom: 1rem;">{model_choice}</h3>
                    <div style="font-size: 3.5rem; font-weight: bold; color: #1E88E5; margin: 1.5rem 0;">
                        {predictions['selected']:.2f} W
                    </div>
                    <div style="color: #666; font-size: 1.1rem;">
                        Predicted Power Output
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Add model-specific information
            model_info = {
                "Gradient Boosting Regressor": "This model excels at capturing complex patterns and typically provides more accurate predictions by combining multiple decision trees.",
                "Linear Regression": "This model offers a straightforward, interpretable prediction based on linear relationships between the input variables."
            }
            
            st.info(f"💡 **Model Information:** {model_info[model_choice]}")

    # Footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: #666;">
            <p>Developed with ❤️ for sustainable energy prediction</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
