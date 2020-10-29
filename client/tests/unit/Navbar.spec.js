import { shallowMount } from '@vue/test-utils';
import Navbar from '../../src/components/Navbar.vue';

describe('Testa Navbar.vue', () => {
    let wrapper;
    beforeEach(() => {wrapper = shallowMount(Navbar)});

    test('Testa se os icones de navegacao aparecem sempre ou nao', () => {
        //Primeiro testa se os icones que devem estar la, estao la
        expect(wrapper.find('.sobre').exists()).toBeTruthy();
        expect(wrapper.find('.informes').exists()).toBeTruthy();
        expect(wrapper.find('.atletas').exists()).toBeTruthy();
        expect(wrapper.find('.campeonatos').exists()).toBeTruthy();
        expect(wrapper.find('.ranking').exists()).toBeTruthy();
        expect(wrapper.find('.cadastro').exists()).toBeFalsy();
        expect(wrapper.find('.campeonato').exists()).toBeFalsy();
        expect(wrapper.find('.partidas').exists()).toBeFalsy();

        //Testa se os icones aparecem com o admin logado
        wrapper.vm.$root = { logado: true, admin:true };
        wrapper.vm.$nextTick(() => {
            expect(wrapper.find('.cadastro').exists()).toBeTruthy();
            expect(wrapper.find('.campeonato').exists()).toBeTruthy();
            expect(wrapper.find('.partidas').exists()).toBeTruthy();
        });
    });
})