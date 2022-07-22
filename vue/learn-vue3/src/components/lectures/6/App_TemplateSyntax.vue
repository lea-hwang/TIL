<template>
	<div>
		<h2>보간법</h2>
		<p>{{ message }}</p>
		<!-- 데이터에 바인딩이 되어있을 때 계속 갱신됨 -->
		<p v-once>{{ message }}</p>
		<!-- v-once: 일회성. 갱신되지 않음-->
		<button v-on:click="message = message + '!'">Click!</button>
		<hr />
		<h2>v-html</h2>
		<p>{{ rawHtml }}</p>
		<p v-html="rawHtml"></p>
		<!-- v-html: html을 보여줌 -->
		<!-- 주의: 웹사이트에서 임의의 HTML을 동적으로 렌더링하면 XSS 취약점(opens new window)으로 쉽게 이어질 수 있음 -->
		<hr />
		<h2>속성 바인딩</h2>
		<div v-bind:title="dynamicTitle">마우스를 올려보세요</div>
		<input type="text" value="홍길동" :disabled="isInputDisabled" />
		<!-- v-bind: 속성에 변수를 연결 -->
		<input v-bind="attrs" />
		<!-- 다중 속성 바인딩 가능 -->
		<h2>Javascript</h2>
		{{ message.split('').reverse().join('') }}
		<br />
		{{ isInputDisabled ? '예' : '아니오' }}
		<!-- {{}} 안에 자바스크립트처럼 작성할 수 있음. -->
	</div>
</template>

<script>
import { ref } from 'vue';
export default {
	setup() {
		const message = ref('안녕하세요!');
		const rawHtml = ref('<strong>안녕하세요</strong>');

		const dynamicTitle = ref('안녕하세요!');
		const isInputDisabled = ref(true);
		const attrs = ref({
			type: 'password',
			value: '123123',
			disabled: false,
		});

		return {
			message,
			rawHtml,
			dynamicTitle,
			isInputDisabled,
			attrs,
		};
	},
};
</script>

<style lang="scss" scoped></style>
