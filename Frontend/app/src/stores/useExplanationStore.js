import {create} from 'zustand'


const ExplanationStore= create((set) => ({
   explanation: '',
   setExplanation: (text) => set({
    explanation: text
   }), 
   clearExplanation: () => set({
    explanation: ''
   })
}));

export default ExplanationStore;