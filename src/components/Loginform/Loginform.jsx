import React from 'react';
import './Loginform.css';
import { AiOutlineFieldTime} from "react-icons/ai";
import { MdOnlinePrediction } from "react-icons/md";
export const Loginform = () => {
  return (
    <div className='wrapper'>
        <form action=''>
            <h1>Electricity  bill prediction</h1>
            <div className="input-box">
                <input type="text" placeholder='Enter a monthly  hours' required />
                <AiOutlineFieldTime className='icon'/>
            </div>
            <div className="input-box">
                <input type="text" placeholder='Number' required />
                <MdOnlinePrediction className='icon'/>
            </div>
            <div className="input-box">
                <input type="text" placeholder='' required />
                <AiOutlineFieldTime className='icon'/>
            </div>
            <div className="input-box">
                <input type="text" placeholder='Number' required />
                <MdOnlinePrediction className='icon'/>
            </div>
            <button type="submit">Submit</button>
            <div>
              <h1>The Electricity bill is :</h1>
            </div>
            
            
        </form>
    </div>
  )
}
