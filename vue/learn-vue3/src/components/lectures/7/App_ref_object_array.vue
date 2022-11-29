<template>
	<div></div>
</template>

<script>
import { reactive, ref } from 'vue';
export default {
	setup() {
		// ref -> object
		const count = ref(0);
		const state = reactive({
			count,
		});
		count.value++;
		console.log(count.value);
		console.log('state.count:', state.count);
		// ref 객체를 object 안에 넣었을 경우 .value를 굳이 붙이지 않아도 된다.

		// ref -> Array
		const message = ref('Hello');
		const arr = reactive([message]);
		console.log('arr[0]:', arr[0].value);
		// ref 객체를 array 안에 넣었을 경우, .value를 해주어야 한다.
		return {};
	},
};
</script>

<style lang="scss" scoped></style>
