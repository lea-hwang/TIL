<template>
	<div>
		<!-- 변수가 참거짓이냐에 따라 class binding 여부가 달라짐 -->
		<!-- <div :class="{ active: isActive, 'text-danger': hasError }">
			텍스트 입니다.
		</div> -->

		<!-- [] 안에 여러 class들을 넣을 수 있고, 삼항연산자도 작성할 수 있음. object도 같이 넣을 수 있음 -->
		<div
			:class="[
				activeClass,
				errorClass,
				isActive ? 'active-class' : 'class',
				classObject,
			]"
		>
			텍스트 입니다.
		</div>

		<!-- <div :class="classObject">텍스트 입니다.</div> -->
		<button @click="toggle">toggle</button>
		<button @click="hasError = !hasError">toggleError</button>
	</div>
</template>

<script>
import { computed, reactive, ref } from 'vue';
export default {
	setup() {
		const isActive = ref(true);
		const hasError = ref(false);
		// const classObject = reactive({
		// 	active: true,
		// 	'text-danger': false,
		// });

		const classObject = computed(() => {
			return {
				active: true,
				'text-danger': false,
				'text-blue': true,
			};
		});
		//computed를 이용한 객체로 넣을 수 잇음

		const activeClass = ref('active');
		const errorClass = ref('error');

		const toggle = () => {
			isActive.value = !isActive.value;
		};

		return { isActive, toggle, hasError, classObject, activeClass, errorClass };
	},
};
</script>

<style scoped>
.active {
	font-weight: 900;
}
.text-danger {
	color: red;
}
</style>
