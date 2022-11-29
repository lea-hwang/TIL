<template>
	<div>
		<p>
			{{ counter }}
		</p>
		<p>
			{{ message }}
		</p>
		<button @click="increment">click!</button>
	</div>
</template>

<script>
import { ref } from 'vue';

export default {
	setup() {
		// props, context가 인자로 들어올 수 있음
		const counter = ref(0);
		const message = ref('Hello Vue3');
		const increment = () => {
			counter.value++;
		};

		return {
			counter,
			message,
			increment,
		};
	},
};
</script>

<style lang="scss" scoped></style>
