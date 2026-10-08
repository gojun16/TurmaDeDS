import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  FlatList,
  TouchableOpacity,
  Modal,
  TextInput,
  Alert,
  SafeAreaView,
  ScrollView,
} from 'react-native';

export default function App() {
  // Lista inicial de receitas
  const [listaReceitas, setListaReceitas] = useState([
    {
      id: '1',
      nome: 'Bolo de Cenoura',
      ingredientes: 'Cenoura, ovos, óleo, açúcar, farinha, fermento',
      modoPreparo: 'Bata os líquidos no liquidificador, misture os secos e asse por 40 min.',
    },
  ]);

  // Estados dos Modais e Formulário
  const [modalFormVisivel, setModalFormVisivel] = useState(false);
  const [modalDetalhesVisivel, setModalDetalhesVisivel] = useState(false);
  const [receitaSelecionada, setReceitaSelecionada] = useState(null);

  // Campos do Formulário
  const [nomeReceita, setNomeReceita] = useState('');
  const [ingredientes, setIngredientes] = useState('');
  const [modoPreparo, setModoPreparo] = useState('');
  
  // Requisito 3: ID para controle de edição (null = cadastrando, string/number = editando)
  const [idEdicao, setIdEdicao] = useState(null);

  // Limpa o formulário e fecha o modal
  const limparEFechar = () => {
    setNomeReceita('');
    setIngredientes('');
    setModoPreparo('');
    setIdEdicao(null);
    setModalFormVisivel(false);
  };

  // Requisito 3: Carrega dados no formulário para edição
  const handleIniciarEdicao = (receita) => {
    setIdEdicao(receita.id);
    setNomeReceita(receita.nome);
    setIngredientes(receita.ingredientes);
    setModoPreparo(receita.modoPreparo);
    setModalDetalhesVisivel(false); // Fecha o modal de detalhes caso esteja aberto
    setModalFormVisivel(true);
  };

  // Salva nova receita ou atualiza existente
  const handleSalvar = () => {
    if (!nomeReceita.trim() || !ingredientes.trim() || !modoPreparo.trim()) {
      Alert.alert('Erro', 'Por favor, preencha todos os campos!');
      return;
    }

    if (idEdicao !== null) {
      // Requisito 3: Edição via .map()
      const listaAtualizada = listaReceitas.map((item) => {
        if (item.id === idEdicao) {
          return {
            ...item,
            nome: nomeReceita,
            ingredientes: ingredientes,
            modoPreparo: modoPreparo,
          };
        }
        return item;
      });
      setListaReceitas(listaAtualizada);
    } else {
      // Cadastro de nova receita
      const novaReceita = {
        id: Date.now().toString(),
        nome: nomeReceita,
        ingredientes: ingredientes,
        modoPreparo: modoPreparo,
      };
      setListaReceitas([...listaReceitas, novaReceita]);
    }

    limparEFechar();
  };

 // Requisito 2: Exclusão com confirmação tratada para Web e Celular
  const handleExcluir = (id) => {
    // Tratamento para Web / Preview do Snack
    if (typeof window !== 'undefined' && window.confirm) {
      const confirmou = window.confirm('Tem certeza que deseja excluir esta receita?');
      if (confirmou) {
        const listaFiltrada = listaReceitas.filter((item) => item.id !== id);
        setListaReceitas(listaFiltrada);
        setModalDetalhesVisivel(false);
      }
      return;
    }

    // Tratamento para dispositivos móveis (Android / iOS)
    Alert.alert(
      'Confirmar Exclusão',
      'Tem certeza que deseja excluir esta receita?',
      [
        { text: 'Cancelar', style: 'cancel' },
        {
          text: 'Excluir',
          style: 'destructive',
          onPress: () => {
            const listaFiltrada = listaReceitas.filter((item) => item.id !== id);
            setListaReceitas(listaFiltrada);
            setModalDetalhesVisivel(false);
          },
        },
      ]
    );
  };

  // Exibe o modal de detalhes da receita
  const handleAbrirDetalhes = (receita) => {
    setReceitaSelecionada(receita);
    setModalDetalhesVisivel(true);
  };

  return (
    <SafeAreaView style={styles.container}>
      {/* Cabeçalho */}
      <View style={styles.header}>
        <Text style={styles.tituloHeader}>📖 Livro de Receitas</Text>
      </View>

      {/* Requisito 1: FlatList e Empty State */}
      <FlatList
        data={listaReceitas}
        keyExtractor={(item) => item.id}
        contentContainerStyle={styles.listaContainer}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={styles.card}
            onPress={() => handleAbrirDetalhes(item)}
          >
            <Text style={styles.cardTitulo}>{item.nome}</Text>
            <View style={styles.cardAcoes}>
              <TouchableOpacity
                style={[styles.btnCard, styles.btnEditar]}
                onPress={() => handleIniciarEdicao(item)}
              >
                <Text style={styles.textoBtnCard}>Editar</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.btnCard, styles.btnExcluir]}
                onPress={() => handleExcluir(item.id)}
              >
                <Text style={styles.textoBtnCard}>Excluir</Text>
              </TouchableOpacity>
            </View>
          </TouchableOpacity>
        )}
        ListEmptyComponent={() => (
          <View style={styles.emptyContainer}>
            <Text style={styles.emptyTexto}>
              📖 Nenhuma receita cadastrada. Toque no + para adicionar!
            </Text>
          </View>
        )}
      />

      {/* Botão Flutuante (+ ou Cadastro) */}
      <TouchableOpacity
        style={styles.btnFlutuante}
        onPress={() => {
          setIdEdicao(null);
          setModalFormVisivel(true);
        }}
      >
        <Text style={styles.textoBtnFlutuante}>+</Text>
      </TouchableOpacity>

      {/* Modal de Formulário (Cadastro / Edição) */}
      <Modal visible={modalFormVisivel} animationType="slide" transparent={true}>
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            {/* Requisito 3: Título dinâmico */}
            <Text style={styles.modalTitulo}>
              {idEdicao ? '✏️ Editar Receita' : '📝 Cadastrar Receita'}
            </Text>

            <TextInput
              style={styles.input}
              placeholder="Nome da Receita"
              value={nomeReceita}
              onChangeText={setNomeReceita}
            />
            <TextInput
              style={[styles.input, styles.inputMultilinha]}
              placeholder="Ingredientes"
              multiline
              value={ingredientes}
              onChangeText={setIngredientes}
            />
            <TextInput
              style={[styles.input, styles.inputMultilinha]}
              placeholder="Modo de Preparo"
              multiline
              value={modoPreparo}
              onChangeText={setModoPreparo}
            />

            <View style={styles.modalBotoes}>
              <TouchableOpacity
                style={[styles.btnModal, styles.btnCancelar]}
                onPress={limparEFechar}
              >
                <Text style={styles.textoBtnModal}>Cancelar</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.btnModal, styles.btnSalvar]}
                onPress={handleSalvar}
              >
                <Text style={styles.textoBtnModal}>Salvar</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>

      {/* Modal de Detalhes da Receita */}
      <Modal visible={modalDetalhesVisivel} animationType="fade" transparent={true}>
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            {receitaSelecionada && (
              <ScrollView>
                <Text style={styles.modalTitulo}>{receitaSelecionada.nome}</Text>
                
                <Text style={styles.subtituloSecao}>Ingredientes:</Text>
                <Text style={styles.textoDetalhe}>{receitaSelecionada.ingredientes}</Text>

                <Text style={styles.subtituloSecao}>Modo de Preparo:</Text>
                <Text style={styles.textoDetalhe}>{receitaSelecionada.modoPreparo}</Text>

                <View style={styles.modalBotoes}>
                  <TouchableOpacity
                    style={[styles.btnModal, styles.btnEditar]}
                    onPress={() => handleIniciarEdicao(receitaSelecionada)}
                  >
                    <Text style={styles.textoBtnModal}>Editar</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={[styles.btnModal, styles.btnExcluir]}
                    onPress={() => handleExcluir(receitaSelecionada.id)}
                  >
                    <Text style={styles.textoBtnModal}>Excluir</Text>
                  </TouchableOpacity>
                </View>

                <TouchableOpacity
                  style={[styles.btnModal, styles.btnFechar, { marginTop: 10 }]}
                  onPress={() => setModalDetalhesVisivel(false)}
                >
                  <Text style={styles.textoBtnModal}>Fechar</Text>
                </TouchableOpacity>
              </ScrollView>
            )}
          </View>
        </View>
      </Modal>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  header: {
    backgroundColor: '#E65100',
    padding: 20,
    alignItems: 'center',
  },
  tituloHeader: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#FFF',
  },
  listaContainer: {
    padding: 15,
    paddingBottom: 80,
  },
  card: {
    backgroundColor: '#FFF',
    borderRadius: 8,
    padding: 15,
    marginBottom: 12,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    elevation: 2,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  cardTitulo: {
    fontSize: 16,
    fontWeight: 'bold',
    flex: 1,
    color: '#333',
  },
  cardAcoes: {
    flexDirection: 'row',
  },
  btnCard: {
    paddingVertical: 6,
    paddingHorizontal: 10,
    borderRadius: 4,
    marginLeft: 6,
  },
  emptyContainer: {
    marginTop: 50,
    alignItems: 'center',
    paddingHorizontal: 20,
  },
  emptyTexto: {
    fontSize: 16,
    color: '#777',
    textAlign: 'center',
  },
  btnFlutuante: {
    position: 'absolute',
    right: 20,
    bottom: 30,
    backgroundColor: '#E65100',
    width: 56,
    height: 56,
    borderRadius: 28,
    justifyContent: 'center',
    alignItems: 'center',
    elevation: 5,
  },
  textoBtnFlutuante: {
    fontSize: 28,
    color: '#FFF',
    lineHeight: 32,
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.5)',
    justifyContent: 'center',
    padding: 20,
  },
  modalContent: {
    backgroundColor: '#FFF',
    borderRadius: 10,
    padding: 20,
    maxHeight: '80%',
  },
  modalTitulo: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 15,
    textAlign: 'center',
    color: '#E65100',
  },
  input: {
    borderWidth: 1,
    borderColor: '#DDD',
    borderRadius: 6,
    padding: 10,
    marginBottom: 12,
    backgroundColor: '#FAFAFA',
  },
  inputMultilinha: {
    height: 70,
    textAlignVertical: 'top',
  },
  modalBotoes: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 10,
  },
  btnModal: {
    flex: 1,
    padding: 12,
    borderRadius: 6,
    alignItems: 'center',
    marginHorizontal: 4,
  },
  btnSalvar: { backgroundColor: '#4CAF50' },
  btnCancelar: { backgroundColor: '#9E9E9E' },
  btnEditar: { backgroundColor: '#2196F3' },
  btnExcluir: { backgroundColor: '#F44336' },
  btnFechar: { backgroundColor: '#757575' },
  textoBtnModal: { color: '#FFF', fontWeight: 'bold' },
  textoBtnCard: { color: '#FFF', fontSize: 12, fontWeight: 'bold' },
  subtituloSecao: { fontWeight: 'bold', marginTop: 10, color: '#333' },
  textoDetalhe: { color: '#555', marginBottom: 10 },
});