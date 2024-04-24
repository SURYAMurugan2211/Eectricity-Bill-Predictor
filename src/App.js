import React, { useState } from 'react';
import axios from 'axios';
import './Loginform.css';

function App() {
    const [formData, setFormData] = useState({
        Fan: '',
        Refrigerator: '',
        Television: '',
        MonthlyHours: ''
    });
    const [prediction, setPrediction] = useState(null);
    const [error, setError] = useState(null);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // Convert input values to numeric
            const numericData = {
                ...formData,
                Fan: parseFloat(formData.Fan),
                Refrigerator: parseFloat(formData.Refrigerator),
                Television: parseFloat(formData.Television),
                MonthlyHours: parseFloat(formData.MonthlyHours)
            };

            const response = await axios.post('http://localhost:8000/api/predict/', numericData);
            setPrediction(response.data.result);
            setError(null);
        } catch (error) {
            console.error('Prediction failed:', error);
            setError('Failed to predict. Please ensure all input values are numeric.');
        }
    };

    return (
        <div className='wrapper'>
            <h2>Electricity bill prediction</h2>
            <form onSubmit={handleSubmit}>
                <div className="input-box">
                    <input type="number" name="Fan" value={formData.Fan} onChange={handleChange} placeholder="Enter Fan hours" />
      
                </div>
                <div className="input-box">
                    <input type="number" name="Refrigerator" value={formData.Refrigerator} onChange={handleChange} placeholder="Enter Refrigerator hours" />
                </div>
                <div className="input-box">
                    <input type="number" name="Television" value={formData.Television} onChange={handleChange} placeholder="Enter Television hours" />
                </div>
                <div className="input-box">
                    <input type="number" name="MonthlyHours" value={formData.MonthlyHours} onChange={handleChange} placeholder="Enter Monthly Hours" />
                </div>
                <button type="submit">Predict</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {prediction && <p><h2>Predicted Electricity bill : {prediction}</h2></p>}
        </div>
    );
}

export default App;

