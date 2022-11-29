<template>
	<div>
		<h2>반응형 메세지</h2>
		<p>{{ reactiveMessage }}</p>
		<button v-on:click="addReactiveMessage">Add Message</button>
		<h2>일반 메세지</h2>
		<p>{{ normalMessage }}</p>
		<button v-on:click="addNormalMessage">Add Message</button>
	</div>
</template>

<script>
import { isRef, onBeforeMount, onMounted, ref } from 'vue';
// isRef: 해당 변수가 reactive한지 여부
// ref: 해당 변수를 reative하게 함
// onMounted: 마운트됐을 때 실행됨
// beforeMounted: 마운트되기 전에 실행됨
export default {
	setup() {
		const reactiveMessage = ref('Hello Reactive message');
		const addReactiveMessage = () => {
			reactiveMessage.value = reactiveMessage.value + '!';
		};
		console.log(isRef(reactiveMessage));

		let normalMessage = 'Hello Normal Message';
		const addNormalMessage = () => {
			normalMessage = normalMessage + '!';
		};
		console.log(isRef(normalMessage));

		onMounted(() => {
			console.log('onMounted');
		});

		onBeforeMount(() => {
			console.log('onBeforeMount');
		});

		return {
			reactiveMessage,
			normalMessage,
			addReactiveMessage,
			addNormalMessage,
		};
	},
};
</script>

<style lang="scss" scoped></style>
