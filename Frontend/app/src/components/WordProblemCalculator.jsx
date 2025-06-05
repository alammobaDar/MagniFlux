import React, {useState} from "react"
import { useMutation } from '@tanstack/react-query'
import VisualStore from '../stores/useVisualStore'
import ExplanationStore from '../stores/useExplanationStore'
import LoadingStore from '../stores/useLoadingStore'
import { SendText } from "../utils/utils"

const WordProblemCalculator = (props) => {
    const [text, setText] = useState("")
    const [flux, setFlux] = useState(null)
    const {setExplanation} = ExplanationStore()
    const {setVisual} = VisualStore()
    const {setLoading} = LoadingStore()

    const {mutate} = useMutation({
        mutationFn: SendText,
        onMutate: () => setLoading(true),
        onSettled: () => setLoading(false)
        ,
        onSuccess: (data) => {
            setFlux(data.result.flux)
            setExplanation(data.result.explanation)
            setVisual(data.visual)
        },
        onError: (error) => {
            alert("Failed to pass the text -> ", error.message)
        }
    }) 

    const handleClick = () =>{
        mutate({'text':text})
    }

    return (
        <div className="flex flex-col w-[430px] h-[600px] bg-[#14121B] rounded-2xl">
            <div className='m-5 pl-5 flex flex-col'>
                <label className="jersey-20-regular text-amber-50 text-3xl">Magnetic Flux</label>
                <div className="flex justify-end items-center w-[350px] h-[130px] pr-3 outline-1 outline-black rounded-lg jersey-20-regular text-amber-50 text-2xl bg-[#1F1D24]">
                    <h1>{flux ?? "--"}</h1>
                    <h1 className="pl-2">Φ</h1>
                </div>
            </div>

            <div className='ml-10 mt-5 flex flex-col textarea-wrapper'>
                <label htmlFor="word-problem" className="jersey-20-regular text-amber-50 text-xl">Word Problem</label>
                <textarea name="word-problem" value={text} id="word-problem" placeholder="Add something..." className="textarea-input" onChange={(e) => setText(e.target.value)}></textarea>
            </div>

            <div className='flex justify-end p-8'>
                <button onClick={handleClick} className='w-20 h-8 bg-[#1F1D24] text-amber-50 jersey-20-regular' >Calculate</button>
            </div>

        </div>
    )
};

export default WordProblemCalculator;
