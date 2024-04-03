import React from "react";

export default function CardTag({tagName, tagColor}) {
    return (
        <div className={"p-1 px-4 border-2 border-slate-600 w-fit rounded-full"} style={}>
            <span className={"text-lg font-semibold"} style={}>{tagName}</span>
        </div>
    );
}
