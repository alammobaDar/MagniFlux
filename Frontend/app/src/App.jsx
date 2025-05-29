import Calculator from './components/Calculator'
import CalculatorExplanation from './components/CalculatorExplanation'
import VisualDisplay from './components/VisualDisplay'
import WordProblemCalculator from './components/WorldProblemCalculator'
import './App.css'

function App() {

  return (
    <div className="flex flex-col h-auto p-20">

      <div className="m-15">
        <h1 className="text-7xl text-gray-400 jersey-20-regular">MagniFlux</h1>
      </div>
    
<<<<<<< HEAD
      <div className="flex gap-7 justify-center">

        <div className="flex flex-col w-[450px] h-[600px] bg-[#14121B] rounded-2xl">

          <div className='m-6 flex justify-center'>
            <input type="text" className='w-[320px] h-[150px] outline-1 outline-black rounded-xl bg-[#1F1D24]'/>
          </div>

          <div className='p-7 flex flex-col gap-y-10'>
            
            <div className='flex flex-col floating-label-wrapper'>
              <input type="text" id='magnetic-field' placeholder='Magnetic Field' className='floating-input' />
              <label htmlFor="magnetic-field" className='floating-label'>Magnetic Field</label>
            </div>

            <div className="flex flex-col floating-label-wrapper">
              <input type="text" id="area" placeholder='Area' className='floating-input' /> 
              <label htmlFor="area" className='floating-label'>Area</label>
            </div>
            
            <div className="flex flex-col floating-label-wrapper">
              <input type="text" id="angle" placeholder='Angle' className='floating-input' /> 
              <label htmlFor="angle" className='floating-label'>Angle</label>
            </div>

          </div>

          <div className='flex justify-end p-8'>
            <button className='w-20 h-8 bg-[#1F1D24] text-amber-50 jersey-20-regular' >Button</button>
          </div>
        </div>
        <div className="w-[700px] h-[600px] bg-[#14121B] rounded-4xl">
          <h1 className='jersey-20-regular text-amber-50'>Text</h1>
        </div>
=======
      <div className="flex flex-wrap gap-7 justify-center">
        <Calculator/>
        <WordProblemCalculator/>

        <CalculatorExplanation/>
        <VisualDisplay/>
>>>>>>> d42dd64 (add calculator ui)
      </div>

    </div>
  )
}

export default App
