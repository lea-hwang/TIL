<template>
	<div>
		<p>{{ message }}</p>
		<button @click="addMessage">add click</button>
	</div>
</template>

<script>
import { reactive, ref } from 'vue';
export default {
	setup() {
		// let message = reactive({
		// 	value: 'Hello',
		// }); // 객체 선언

		let message = ref('Hello');
		// ref: primitive 반응형 데이터 (number, string, boolean)
		// ref 메서드는 변이가능한(mutable) 객체를 반환함. 이 객체 안에는 value 값에 대한 반응형 참조(reference) 역할을 한다

		const addMessage = () => {
			message.value = message.value + '!';
		};
		console.log('message');
		console.log('message:', message.value);
		console.log('message typeof:', typeof message.value);

		return {
			message,
			addMessage,
		};
	},
};
</script>

<style lang="scss" scoped></style>
