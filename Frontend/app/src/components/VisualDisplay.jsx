import React from "react";
import Plot from 'react-plotly.js';
import VisualStore from '../stores/useVisualStore';

const VisualDisplay = () => {
  const { visual } = VisualStore();

  return (
    <div className="flex items-center justify-center w-[700px] h-[600px] bg-[#14121B] rounded-4xl">
      {visual ? (
        <Plot
          data={visual.data}
          layout={{
            ...visual.layout,
            autosize: false,
            width: 600,
            height: 500,
            margin: { t: 50, b: 50, l: 50, r: 50 },
          }}
          config={{ responsive: true }}
          style={{ width: '600px', height: '500px' }}
          useResizeHandler={false} 
        />
      ) : (
        <p className="jersey-20-regular text-6xl text-amber-50">Loading Visualization...</p>
      )}
    </div>
  );
};

export default VisualDisplay;
  