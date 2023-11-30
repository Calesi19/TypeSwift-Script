<script>
	import "./app.css";
  import { AccordionItem, Accordion } from 'flowbite-svelte';
</script>


<style>
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>


<main>
	<h1 class="text-2xl">Hello!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>

	  
	  <Accordion>
		<AccordionItem>
		  <span slot="header mb-20">My Header 1</span>
		  <p class="mb-2 text-gray-500 dark:text-gray-400">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo ab necessitatibus sint explicabo ...</p>
		  <p class="text-gray-500 dark:text-gray-400">
			Check out this guide to learn how to <a href="/" target="_blank" rel="noreferrer" class="text-blue-600 dark:text-blue-500 hover:underline"> get started </a>
			and start developing websites even faster with components on top of Tailwind CSS.
		  </p>
		</AccordionItem>
		<AccordionItem>
		  <span slot="header">My Header 2</span>
		  <p class="mb-2 text-gray-500 dark:text-gray-400">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo ab necessitatibus sint explicabo ...</p>
		  <p class="mb-2 text-gray-500 dark:text-gray-400">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Illo ab necessitatibus sint explicabo ...</p>
		  <p class="mb-2 text-gray-500 dark:text-gray-400">Learn more about these technologies:</p>
		  <ul class="list-disc pl-5 dark:text-gray-400 text-gray-500">
			<li>
			  <a href="/" target="_blank" rel="noreferrer" class="text-blue-600 dark:text-blue-500 hover:underline"> Lorem ipsum </a>
			</li>
			<li>
			  <a href="https://tailwindui.com/" rel="noreferrer" target="_blank" class="text-blue-600 dark:text-blue-500 hover:underline"> Tailwind UI </a>
			</li>
		  </ul>
		</AccordionItem>
	  </Accordion>


</main>


