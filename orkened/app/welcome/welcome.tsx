import logo from "./namn.webp";
import { Combobox, ComboboxInput, ComboboxOption, ComboboxOptions } from '@headlessui/react'
import { useState } from 'react'
import { words, Word} from "./ord"
import uttryck from "./uttryck"
import Fuse, {FuseResult} from 'fuse.js'


const options = {
    // isCaseSensitive: true,
    // includeScore: false,
    shouldSort: true,
    // includeMatches: false,
    // findAllMatches: false,
    // minMatchCharLength: 1,
    // location: 0,
    // threshold: 0.6,
    // distance: 100,
    // useExtendedSearch: false,
    // ignoreLocation: false,
    // ignoreFieldNorm: false,
    // fieldNormWeight: 1,
    keys: [
        "riks",
        "dialekt",
    ],
}
const fuse = new Fuse(words, options);

export function Welcome() {
    const [selectedWord, setSelectedWord] = useState<FuseResult<Word>>()
    const [query, setQuery] = useState('')

    const filteredWords = fuse.search(query, {limit: 5})

    return (
	<main className="flex items-center justify-center pt-16 pb-4">
	    <div className="flex-1 flex flex-col items-center gap-16 min-h-0">
		<header className="flex flex-col items-center gap-9">
		    <div className="w-[300px] max-w-[100vw] p-4">
			<img
			    src={logo}
				alt="Örkeneds Dialekten"
				className="block w-full"
			/>
		    </div>
		</header>

		<div className="max-w-[300px] w-full space-y-6 px-4">
		    <Combobox onChange={setSelectedWord} onClose={() => setQuery('')}>
			<ComboboxInput
			    className="border border-black" aria-label="Ord" displayValue={(word: any) => word.item.riks}
			    onChange={(event) => setQuery(event.target.value)}
			/>	  
			<ComboboxOptions anchor="bottom" className="border">
			    {filteredWords.map((word) => (
				<ComboboxOption key={word.item.riks} value={word} className="data-focus:bg-blue-100">
				    {word.item.riks}
				</ComboboxOption>
			    ))}
			</ComboboxOptions>
		    </Combobox>		    
		</div>
		<div className="max-w-[300px] w-full space-y-6 px-4">
		    <div className="flex flex-row gap-x-16">
			<div>
			    {selectedWord?.item.riks}
			</div>
			<div>
			    {selectedWord?.item.dialekt}
			</div>
  		    </div>
		    <div>
			<audio controls>
			    <source src={selectedWord?.item.audio} type="audio/wav"/>
			</audio>
		    </div>
		</div>
	    </div>
	</main>
    );
			}
