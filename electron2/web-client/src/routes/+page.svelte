<script>
	import { Card, Button } from 'flowbite-svelte';
	import {
		Table,
		Input,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
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

  import ShortcutRow from './components/ShortcutRow.svelte'
  import EmptyResults from './components/EmptyResults.svelte'
</script>

<div class="w-full min-h-[100vh] py-10 flex flex-col items-center background">
	<h1 class="my-10 font-[Racing] text-6xl text-blue-900">
		Type<span class="text-[#EB4F26]">Swift</span>
	</h1>

	<div class="container flex flex-col items-center justify-center">
		<Card size="lg">
			<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
				Create your own shortcuts
			</h5>
			<p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">
				Enter a username or id you would like to use to sync up your shortcuts. Keep in mind that this is public and anyone that loads your username can see your shortcuts.
			</p>

      <div class="flex mt-10">
        <Input class="mr-3" id="default-input" placeholder="Public Username" />

        <Button>
          Load
        </Button>

      </div>

			<Table class="mt-6">
				<TableHead>
					<TableHeadCell>Shortcut</TableHeadCell>
					<TableHeadCell>Phrase</TableHeadCell>
					<TableHeadCell>Options</TableHeadCell>
				</TableHead>
				<TableBody>
          <ShortcutRow />
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

					<TableBodyRow>
						<TableBodyCell>Microsoft Surface Pro</TableBodyCell>
						<TableBodyCell>White</TableBodyCell>
					</TableBodyRow>
					<TableBodyRow>
						<TableBodyCell>Magic Mouse 2</TableBodyCell>
						<TableBodyCell>Black</TableBodyCell>
					</TableBodyRow>
          
				</TableBody>
			</Table>

      <EmptyResults />

			<div class="my-2 flex justify-end gap-2">
				<Button>Save</Button>
				<Button color="alternative">Download JSON</Button>
			</div>
		</Card>
	</div>
</div>

<style>
	@font-face {
		font-family: 'Agbalumo';
		src: url('/fonts/Agbalumo-Regular.ttf') format('truetype');
	}

	@font-face {
		font-family: 'Racing';
		src: url('/fonts/RacingSansOne-Regular.ttf') format('truetype');
	}

	.background {
		background-image: linear-gradient(35deg, #e6e4fd 10%, #f3fcff 60%);
	}
</style>
