import { BlockMath } from 'react-katex'
import ExplanationStore from '../stores/useExplanationStore'
const CalculatorExplanation = (props) => {
    const {explanation} = ExplanationStore();
    return (
        <div className="p-10 relative w-[600px] h-[600px] bg-[#14121B] rounded-4xl">
            <h1 className="jersey-20-regular text-amber-50 text-3xl">Formula:</h1>
            <div className="m-7 h-8 flex justify-center items-center jersey-20-regular text-2xl text-amber-50 formula">
                <BlockMath math="\Phi = B \cdot A \cdot \cos(\theta)"/>
            </div>
            <h1 className="jersey-20-regular text-amber-50 text-3xl">Explanation:</h1>

            <div className="h-72 my-7 flex justify-center items-center jersey-20-regular text-2xl overflow-y-scroll text-amber-50 formula">
                <h1 className="jersey-20-regular text-2xl text-amber-50">{explanation}</h1>
            </div>
        </div> 
    )
};

export default CalculatorExplanation;
