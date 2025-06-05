import { create } from "zustand";


const VisualStore = create((set) => ({
    visual: null,
    setVisual: (image) => set({
        visual: image
    }),
    clearVisual: () => set({
        visual: null
    })
}))

export default VisualStore