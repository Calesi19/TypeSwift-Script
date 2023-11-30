<script>
    // Export component

	import { Button } from 'flowbite-svelte';
	import {
		Input,
		TableBodyCell,
		TableBodyRow,
	} from 'flowbite-svelte';
	import { Textarea } from 'flowbite-svelte';
	import { TrashBinSolid } from 'flowbite-svelte-icons';
	let textareaprops = {
		id: 'message',
		name: 'message',
		label: 'Your text',
		rows: 4,
		placeholder: 'Type your text here...'
	};

</script>

<TableBodyRow>
    <TableBodyCell><Input id="default-input" placeholder="shorthand" /></TableBodyCell>
    <TableBodyCell>
        <Textarea {...textareaprops} />
    </TableBodyCell>
    <TableBodyCell>
        <Button color="light">
            <TrashBinSolid class="w-5 h-5 text-slate-500 hover:text-red-700" />
        </Button>
    </TableBodyCell>
</TableBodyRow>


