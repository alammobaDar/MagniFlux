import React from "react"

const Calculator  = (props) => {
  return (
    <div className="flex flex-col w-[430px] h-[600px] bg-[#14121B] rounded-2xl">
        <div className='m-5 pl-5 flex flex-col'>
            <label htmlFor="output" className="jersey-20-regular text-amber-50 text-3xl">Magnetic Flux</label>
            <input type="text" id="output" className='w-[350px] h-[130px] outline-1 outline-black rounded-lg jersey-20-regular text-right text-amber-50 text-2xl bg-[#1F1D24]' disabled/>
        </div>
        <div className='pl-10 pt-7 flex flex-col gap-y-10'>

            <div className='flex floating-label-wrapper'>
                <input type="text" id='magnetic-field' placeholder='Magnetic Field' className='floating-input' />
                <label htmlFor="magnetic-field" className='floating-label'>Magnetic Field</label>
                <h1 className="p-3 jersey-20-regular text-amber-50 text-lg align-middle">Tesla(T)</h1>  
            </div>

            <div className="flex floating-label-wrapper">
                <input type="text" id="area" placeholder='Area' className='floating-input' /> 
                <label htmlFor="area" className='floating-label'>Area</label>
                <h1 className="p-3 jersey-20-regular text-amber-50 text-lg align-middle">Area(m²)</h1>
            </div>
            
            <div className="flex floating-label-wrapper">
                <input type="text" id="angle" placeholder='Angle' className='floating-input' /> 
                <label htmlFor="angle" className='floating-label'>Angle</label>
                <h1 className="p-3 jersey-20-regular text-amber-50 text-lg align-middle">Degrees(°)</h1>
            </div>
        </div>

        <div className='flex justify-end p-8'>
            <button className='w-20 h-8 bg-[#1F1D24] text-amber-50 jersey-20-regular' >Button</button>
        </div>

    </div>



  )
};

export default Calculator ;
