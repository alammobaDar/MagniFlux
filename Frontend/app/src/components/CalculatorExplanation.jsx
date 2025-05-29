import React from "react"
import { BlockMath } from 'react-katex'
const CalculatorExplanation = (props) => {
    return (
        <div className="p-10 w-[600px] h-[600px] bg-[#14121B] rounded-4xl">
            <h1 className="jersey-20-regular text-amber-50 text-3xl">Formula:</h1>
            <div className="m-11 flex justify-center items-center jersey-20-regular text-2xl text-amber-50 formula">
                <BlockMath math="\Phi = B \cdot A \cdot \cos(\theta)"/>
            </div>
            <h1 className="jersey-20-regular text-amber-50 text-3xl">Explanation:</h1>

            
        </div>
    )
};

export default CalculatorExplanation;
