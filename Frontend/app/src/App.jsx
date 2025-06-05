import Calculator from './components/Calculator'
import CalculatorExplanation from './components/CalculatorExplanation'
import VisualDisplay from './components/VisualDisplay'
import WordProblemCalculator from './components/WordProblemCalculator'
import LoadingSpinner from './components/LoadingSpinner'
import './App.css'
import swap from './assets/alter.png'
import { useState } from 'react'
import LoadingStore from './stores/useLoadingStore'
import VisualStore from './stores/useVisualStore'
import ExplanationStore from './stores/useExplanationStore'

function App() {
    const [show, setShow] = useState(true)
    const {isLoading} = LoadingStore()
    const {clearExplanation} = ExplanationStore()
    const {clearVisual} = VisualStore()
    
    const swapPanels = () =>{
        setShow((prev) => !prev)
        clearExplanation()
        clearVisual()
    }
    return (
        <div className="flex flex-col h-auto p-20">
            {isLoading &&(
                <div className="fixed top-0 left-0 w-full h-full bg-black bg-opacity-30 z-50 flex items-center justify-center">
                    <LoadingSpinner />
                </div>
            )}
            <div className="m-15">
                <h1 className="text-7xl text-gray-400 jersey-20-regular">MagniFlux</h1>
            </div>

            <div className="flex flex-wrap gap-7 justify-center">
                
                <button onClick={swapPanels}>
                    <img className="w-[50px] h-[50px]" src={swap} alt="swap" />
                </button>
            
                {show ? (
                    <Calculator/>
                ):(
                    <WordProblemCalculator/>
                )}
                <CalculatorExplanation/>
                <VisualDisplay/>
            </div>

        </div>
    )
  }

export default App
