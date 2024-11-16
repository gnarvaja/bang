'use client';
import {Tokens} from "~~/models/Token";
import {fetchPriceFromPyth} from "~~/utils/pyth/fetchPriceFromPyth";
import {useState} from "react";

const UpdatePythPrice: React.FC = () => {

    const [tokenInput, setTokenInput] = useState<string>(Tokens.UNI.id);



    return (
        <div className="flex flex-col gap-y-6 lg:gap-y-8 py-8 lg:py-12 justify-center items-center">
            <input
                value={tokenInput} onInput={e => setTokenInput(e.target.value)}
                className={`input`}
            />
            <button
                className={`btn btn-secondary btn-sm font-light hover:border-transparent`}
                onClick={async () => {
                    const pythPrice = await fetchPriceFromPyth(tokenInput);
                    alert(`Pyth price for ${tokenInput}: ${pythPrice}`);
                }}
            >
                Update Pyth Price in {"Hardhat"}
            </button>
        </div>
    );
};

export default UpdatePythPrice;
