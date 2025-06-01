import React from "react"
import Plot from 'react-plotly.js';

const VisualDisplay = ({visual}) => {
  return (
    <div className=" flex items-center justify-center w-[700px] h-[600px] bg-[#14121B] rounded-4xl">
          {visual ? (
            <div className="">
              <Plot
                data={visual.data}
                layout={visual.layout}
                config={{responsive: true}}
              />
            </div>
          ):(
            <p className="jersey-20-regular text-6xl text-amber-50">Loading Visualization...</p>
          )}
    </div>
  )
};

export default VisualDisplay;
