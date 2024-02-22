<script>
	import { Input, Textarea, Toast } from "flowbite-svelte";

	let username = "";
	let email = "";
	let message = "";

	/**
	 * @param {{ preventDefault: () => void; }} event
	 */
	async function handleSubmit(event) {
		event.preventDefault();

		const data = {
			username,
			email,
			message,
		};
		console.log(data);

		const server_api = import.meta.env.VITE_API_ADDRESS;
		// Send the form data to the server
		fetch(`${server_api}/api/send_email`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data),
		}).then((response) => {
			if (response.ok) {
				document.querySelector(".mx-auto.max-w-lg.text-center.flex.justify-center.m-2").style.display = "flex";
			}
		});
	}
</script>

<main>
	<div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
		<div class="mx-auto max-w-lg text-center flex justify-center m-2" style="display: none;">
			<Toast
				dismissable={true}
			>
				<div class="ps-4 text-sm font-normal">
					Message sent successfully.
				</div>
			</Toast>
		</div>

		<div class="mx-auto max-w-lg text-center">
			<h1 class="text-2xl font-bold sm:text-3xl text-gray-100">
				Connect with me!
			</h1>

			<p class="mt-4 text-gray-400">
				Have a question or want to work together? I'd love to hear from
				you! Send me a message and I'll respond as soon as possible.
			</p>
		</div>

		<form
			action="#"
			class="mx-auto mb-0 mt-8 max-w-md space-y-4"
			on:submit={handleSubmit}
		>
			<div>
				<label for="name" class="sr-only">Name</label>

				<div class="relative">
					<Input
						bind:value={username}
						placeholder="Your name"
						required
					/>
				</div>
			</div>

			<div>
				<label for="email" class="sr-only">Email</label>

				<div class="relative">
					<Input
						label="Email"
						type="email"
						bind:value={email}
						name="email"
						required
						placeholder="Your email"
					/>
				</div>
			</div>

			<div>
				<label for="message" class="sr-only">message</label>

				<div class="relative">
					<Textarea
						bind:value={message}
						label="Message"
						rows="4"
						placeholder="Your message"
						required
					/>
				</div>
			</div>

			<div class="flex items-center justify-center">
				<button
					id="submit"
					type="submit"
					class="inline-block rounded-lg bg-violet-500 px-5 py-3 text-sm font-medium text-white"
				>
					Connect with me
				</button>
			</div>
		</form>

		<div class="footer mt-16 text-center">
			<p class="text-gray-500">
				Made with ❤️ by{" "}
				<a
					href="https://singhsujeet0.web.app"
					class="text-violet-500"
					target="_blank"
					rel="noopener noreferrer">Sujeet</a
				>
			</p>
		</div>
	</div>
</main>
