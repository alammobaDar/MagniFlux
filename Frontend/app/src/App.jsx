import Calculator from './components/Calculator'
import CalculatorExplanation from './components/CalculatorExplanation'
import VisualDisplay from './components/VisualDisplay'
import WordProblemCalculator from './components/WordProblemCalculator'
import LoadingSpinner from './components/LoadingSpinner'
import './App.css'
import swap from './assets/alter.png'
import { useState } from 'react'

function App() {
    const [show, setShow] = useState(true)
    const [magneticField, setMagneticField] = useState("")
    const [area, setArea] = useState("")
    const [angle, setAngle] = useState("")
    const [flux, setFlux] = useState(null)
    const [angleUnit, setAngleUnit] = useState("Degrees")
    const [text, setText] = useState("")
    const [explain, setExplain] = useState("")
    const [isLoading, setLoading] = useState(false)
    

    const swapPanels = () =>{
        setShow((prev) => !prev)
    }
    return (
        <div className="flex flex-col h-auto p-20">
            {isLoading && <LoadingSpinner/>}
            <div className="m-15">
                <h1 className="text-7xl text-gray-400 jersey-20-regular">MagniFlux</h1>
            </div>

            <div className="flex flex-wrap gap-7 justify-center">
                
                <button onClick={swapPanels}>
                    <img className="w-[50px] h-[50px]" src={swap} alt="swap" />
                </button>
            
                {show ? (
                    <Calculator
                        magneticField={magneticField}
                        setMagneticField={setMagneticField}
                        area={area}
                        setArea={setArea}
                        angle={angle}
                        setAngle={setAngle}
                        flux={flux}
                        setFlux={setFlux}
                        angleUnit={angleUnit}
                        setAngleUnit={setAngleUnit}
                        setExplain={setExplain}
                        setLoading={setLoading}
                    />
                ):(
                    <WordProblemCalculator
                        text={text}
                        setText={setText}
                        flux={flux}
                        setFlux={setFlux}
                        setExplain={setExplain}
                        setLoading={setLoading}
                    />
                )}
                <CalculatorExplanation
                    explain={explain}
                />
                <VisualDisplay/>
            </div>

        </div>
    )
  }

export default App
