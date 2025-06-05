import React, { useState, useEffect, useRef } from "react"
import { useMutation } from "@tanstack/react-query";
import ExplanationStore from '../stores/useExplanationStore'
import VisualStore from '../stores/useVisualStore'
import LoadingStore  from '../stores/useLoadingStore'
import {isValid}from '../utils/validators'
import {SendInputsForExplanation} from '../utils/utils'

const Calculator  = (props) => {
    const [magneticField, setMagneticField] = useState("")
    const [area, setArea] = useState("")
    const [angle, setAngle] = useState("")
    const [angleUnit, setAngleUnit] = useState("Degrees")
    const [flux, setFlux] = useState(null)
    const {setExplanation} = ExplanationStore()
    const {setVisual, clearVisual} = VisualStore()
    const {setLoading} = LoadingStore()
    const [trigger, setTrigger] = useState(false)

    const calculateFlux = () =>{
        const B = parseFloat(magneticField)
        const A = parseFloat(area)
        let theta = parseFloat(angle)

        if(isValid(B,A,theta,angleUnit)){
            if (angleUnit === "Degrees"){
                theta = theta * (Math.PI/180)
            }
            // console.log(theta)
            const result = B * A * Math.cos(theta)
            setFlux(result.toFixed(4))
            }
    }

    const {mutate} = useMutation({
        mutationFn: SendInputsForExplanation,
        onMutate: () => setLoading(true),
        onSettled: () => setLoading(false),
        onSuccess: (data) => {
            setExplanation(data.result.explanation)
            setVisual(data.visual)
        },
        onError: (error) => {
            alert("Failed to pass the text -> ", error.message)
        }
    }) 

    const handleClick = () =>{
        console.log("click")
        calculateFlux();
        setTrigger(true)
    }

    useEffect(() => {
        if (flux != null && trigger){
            mutate({
                'Tesla': magneticField,
                'Area': area,
                'Angle': angle,
                'angleUnits': angleUnit,
                'flux':flux
            });
            setTrigger(false)
        }
    }, [flux, trigger])

    return (
        <div className="flex flex-col w-[430px] h-[600px] bg-[#14121B] rounded-2xl">
            <div className='m-5 pl-5 flex flex-col'>
                <label className="jersey-20-regular text-amber-50 text-3xl">Magnetic Flux</label>
                <div className="flex justify-end items-center w-[350px] h-[130px] pr-3 outline-1 outline-black rounded-lg jersey-20-regular text-amber-50 text-2xl bg-[#1F1D24]">
                    <h1>{flux ?? "--"}</h1>
                    <h1 className="pl-2">Φ</h1>
                </div>
            </div>
            <div className='pl-10 pt-7 flex flex-col gap-y-10'>

                <div className='flex floating-label-wrapper'>
                    <input type="text" value={magneticField} id='magnetic-field' placeholder='Magnetic Field' className='floating-input' onChange={(e) => setMagneticField(e.target.value)}/>
                    <label htmlFor="magnetic-field" className='floating-label'>Magnetic Field</label>
                    <h1 className="p-3 jersey-20-regular text-amber-50 text-lg align-middle">Tesla(T)</h1>  
                </div>

                <div className="flex floating-label-wrapper">
                    <input type="text" value={area} id="area" placeholder='Area' className='floating-input' onChange={(e) => setArea(e.target.value)}/> 
                    <label htmlFor="area" className='floating-label'>Area</label>
                    <h1 className="p-3 jersey-20-regular text-amber-50 text-lg align-middle">Area(m²)</h1>
                </div>
                
                <div className="flex floating-label-wrapper">
                    <input type="text" value={angle} id="angle" placeholder='Angle' className='floating-input' onChange={(e) => setAngle(e.target.value)}/> 
                    <label htmlFor="angle" className='floating-label'>Angle</label>
                    <select id="angle" value={angleUnit} className="p-3 jersey-20-regular text-amber-50 text-lg align-middle" onChange={(e) => setAngleUnit(e.target.value)}>
                        <option value="Degrees">Degrees(°)</option>
                        <option value="Radians">Radians(c)</option>
                    </select>
                </div>
            </div>

            <div className='flex justify-end p-8'>
                <button onClick={handleClick} className='w-20 h-8 bg-[#1F1D24] text-amber-50 jersey-20-regular' >Calculate</button>
            </div>

        </div>

    )
};

export default Calculator ;
