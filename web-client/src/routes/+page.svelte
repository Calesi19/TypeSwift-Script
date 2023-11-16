<script>
    import { Card, Button } from 'flowbite-svelte';
    import { Table, Input, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
    import { Textarea } from 'flowbite-svelte';
    let textareaprops = {
    id: 'message',
    name: 'message',
    label: 'Your text',
    rows: 4,
    placeholder: 'Type your text here...'
  };
  </script>


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
        background-image: linear-gradient(35deg,#e6e4fd 10%,#f3fcff 60%);

    }

</style>


<div class="w-full min-h-[100vh] py-10 flex flex-col items-center background">

<h1 class="my-10 font-[Racing] text-6xl text-blue-900">TypeSwift</h1>

<div class="container flex flex-col items-center justify-center">
   
    <Card size="lg">
        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Noteworthy technology acquisitions 2021</h5>
        <p class="font-normal text-gray-700 dark:text-gray-400 leading-tight">Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.</p>
    

      <Table class="mt-6" >
        <TableHead>
          <TableHeadCell>Shortcut</TableHeadCell>
          <TableHeadCell>Phrase</TableHeadCell>
        </TableHead>
        <TableBody>
          <TableBodyRow>
            <TableBodyCell><Input id="default-input" placeholder="shorthand" /></TableBodyCell>
            <TableBodyCell>
                <Textarea {...textareaprops} />

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

    <div class="my-2 flex justify-end gap-2">
        <Button >Save</Button>
        <Button color="alternative">Sync</Button>
    </div>
    
    </Card>

</div>

</div>