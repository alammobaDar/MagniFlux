import { create } from "zustand";

const LoadingStore = create((set) => ({
    isLoading: false,
    setLoading: (loading) => set({
        isLoading: loading
    })
}))

export default LoadingStore;